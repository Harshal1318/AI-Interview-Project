from llm import ask_llama

def evaluate_answer(question, answer):

    prompt = f"""
Question:

{question}

Answer:

{answer}

Evaluate answer.

Return:

Score /10

Strengths

Weaknesses

Ideal Answer
"""

    return ask_llama(prompt)