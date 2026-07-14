import streamlit as st

from resume_parser import extract_text
from resume_analyzer import analyze_resume
from question_generator import generate_questions
from answer_evaluator import evaluate_answer

# ======================
# Page Config
# ======================

st.set_page_config(
    page_title=" InterviewPilot AI",
    layout="wide"
)

st.title(" InterviewPilot AI")
st.markdown("### AI-Powered Mock Interview Platform")

# ======================
# Resume Upload
# ======================

uploaded_file = st.file_uploader(
    "Upload Resume",
    type=["pdf"]
)

if uploaded_file:

    resume_text = extract_text(uploaded_file)

    st.success(" Resume Uploaded Successfully")

    # ======================
    # Interview Settings
    # ======================

    st.divider()

    st.header("⚙️ Interview Settings")

    role = st.selectbox(
        "Target Role",
        [
            "AI Engineer",
            "Machine Learning Engineer",
            "Computer Vision Engineer",
            "Data Scientist",
            "Software Engineer"
        ]
    )

    difficulty = st.selectbox(
        "Difficulty",
        [
            "Beginner",
            "Intermediate",
            "Advanced"
        ]
    )

    interview_type = st.selectbox(
        "Interview Type",
        [
            "Technical",
            "Project",
            "HR",
            "Mixed"
        ]
    )

    num_questions = st.slider(
        "Number of Questions",
        min_value=5,
        max_value=30,
        value=10,
        step=5
    )

    # ======================
    # Action Buttons
    # ======================

    col1, col2 = st.columns(2)

    with col1:

        if st.button("📄 Analyze Resume"):

            with st.spinner("Analyzing Resume..."):

                analysis = analyze_resume(
                    resume_text
                )

                st.session_state[
                    "analysis"
                ] = analysis

    with col2:

        if st.button(" Generate Questions"):

            with st.spinner(
                "Generating Questions..."
            ):
                questions = generate_questions(
                    resume_text,
                    role,
                    difficulty,
                    interview_type,
                    num_questions
                )

                st.session_state["questions"]=questions

    # ======================
    # Resume Analysis
    # ======================

    if "analysis" in st.session_state:

        st.divider()

        st.header("📊 Resume Analysis")

        st.write(
            st.session_state[
                "analysis"
            ]
        )

# ======================
# Questions Section
# ======================

questions_text = st.session_state.get("questions")

if questions_text is not None and questions_text != "":

    st.divider()

    st.header(" Generated Questions")

    questions_list = []

    for line in questions_text.split("\n"):

        line = line.strip()

        if not line:
            continue

        # Accept:
        # 1. Question
        # 1) Question
        if line[0].isdigit():

            if "." in line:
                question = line.split(".", 1)[1].strip()

            elif ")" in line:
                question = line.split(")", 1)[1].strip()

            else:
                question = line

            questions_list.append(question)

    st.success(
        f"{len(questions_list)} Questions Generated"
    )

    # Debug (remove later)
    with st.expander("List of questions"):
        st.code(questions_text)

    if len(questions_list) > 0:

        selected_question = st.selectbox(
            "Choose a Question",
            questions_list
        )

        st.session_state[
            "selected_question"
        ] = selected_question

    else:

        st.warning(
            "No questions were extracted from the model output."
        )
# ======================
# Selected Question
# ======================

if "selected_question" in st.session_state:

    st.divider()

    st.header("🎤 Interview Question")

    st.info(
        st.session_state[
            "selected_question"
        ]
    )

    answer = st.text_area(
        "Write Your Answer",
        height=250
    )

    if st.button(
        "Submit Answer"
    ):

        if answer.strip() == "":

            st.warning(
                "Please enter an answer."
            )

        else:

            with st.spinner(
                "Evaluating Answer..."
            ):

                feedback = evaluate_answer(
                    st.session_state[
                        "selected_question"
                    ],
                    answer
                )

                st.session_state[
                    "feedback"
                ] = feedback

                st.session_state[
                    "last_question"
                ] = st.session_state[
                    "selected_question"
                ]

# ======================
# Feedback
# ======================

if "feedback" in st.session_state:

    st.divider()

    st.header(" Interview Feedback")

    st.markdown(
        f"### Question\n\n{st.session_state['last_question']}"
    )

    st.write(
        st.session_state[
            "feedback"
        ]
    )