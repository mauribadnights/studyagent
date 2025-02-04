import json
import uuid
import os

def save_questions(pdf_path, questions):
    base_name = os.path.basename(pdf_path).split('.')[0]
    os.makedirs(f"questions/{base_name}", exist_ok=True)
    
    for q in questions:
        q['id'] = str(uuid.uuid4())
        with open(f"questions/{base_name}/{q['id']}.json", 'w') as f:
            json.dump(q, f)

def load_questions(pdf_path):
    base_name = os.path.basename(pdf_path).split('.')[0]
    questions = []
    for file in os.listdir(f"questions/{base_name}"):
        with open(f"questions/{base_name}/{file}") as f:
            questions.append(json.load(f))
    return questions

def update_scores(score_file, q_id, result):
    try:
        with open(score_file) as f:
            scores = json.load(f)
    except FileNotFoundError:
        scores = {}
    
    if q_id not in scores:
        scores[q_id] = {'correct': 0, 'partial': 0, 'wrong': 0}
    
    scores[q_id][result] += 1
    with open(score_file, 'w') as f:
        json.dump(scores, f)