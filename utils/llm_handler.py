import openai
import json
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_questions(text, num_questions, types):
    prompt = f"""Generate {num_questions} questions per type ({', '.join(types)}) from this text:
    {text[:3000]}...
    Format: JSON list with 'id', 'type', 'question', 'answer', and 'choices' (if MCQ)."""
    
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return json.loads(response.choices[0].message.content)

def evaluate_answer(correct, user_answer):
    prompt = f"""Compare answers:
    Correct: {correct}
    User: {user_answer}
    Respond ONLY with 'correct', 'partial', or 'wrong'."""
    
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content.lower()