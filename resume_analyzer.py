from llm import ask_llama

def analyze_resume(resume_text):

    prompt = f"""
You are an ATS Resume Analyzer.

Analyze this resume.

Return:

Resume Score /100

Top Skills

Strengths

Weaknesses

Missing Skills for AI Engineer

Resume:

{resume_text}
"""

    return ask_llama(prompt)