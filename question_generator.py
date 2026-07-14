from llm import ask_llama

def generate_questions(
        resume_text,
        role,
        difficulty,
        interview_type,
        num_questions
        ):

    prompt = f"""
Generate EXACTLY {num_questions} interview questions.

Role: {role}
Difficulty: {difficulty}
Interview Type: {interview_type}

Rules:
- Generate EXACTLY {num_questions} questions.
- Number every question as:
1.
2.
3.
...
- One question per line.
- No headings.
- No explanations.
- No notes.
- Stop after question {num_questions}.
"""
    response = ask_llama(prompt)
    return response