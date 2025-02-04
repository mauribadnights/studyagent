import argparse
import os
from utils.pdf_reader import extract_text
from utils.llm_handler import generate_questions, evaluate_answer
from utils.file_manager import save_questions, load_questions, update_scores

def main():
    parser = argparse.ArgumentParser(description='Generate and answer questions from PDF')
    parser.add_argument('pdf_path', help='Path to PDF document')
    parser.add_argument('-n', '--num_questions', type=int, default=3, 
                      help='Number of questions per type')
    parser.add_argument('-t', '--types', nargs='+', default=['mcq', 'short'],
                      choices=['mcq', 'short', 'long'], help='Question types to generate')
    args = parser.parse_args()

    # Extract text and generate questions
    text = extract_text(args.pdf_path)
    questions = generate_questions(text, args.num_questions, args.types)
    save_questions(args.pdf_path, questions)

    # Quiz session
    score_file = f"scores_{os.path.basename(args.pdf_path)}.json"
    for q in load_questions(args.pdf_path):
        print(f"\n[{q['type'].upper()}] {q['question']}")
        if q['type'] == 'mcq':
            for i, choice in enumerate(q['choices']):
                print(f"{i+1}. {choice}")
        
        user_answer = input("Your answer: ")
        
        if q['type'] == 'mcq':
            correct = str(user_answer).strip().lower() == q['answer'].strip().lower()
            result = 'correct' if correct else 'wrong'
        else:
            result = evaluate_answer(q['answer'], user_answer)
        
        update_scores(score_file, q['id'], result)
        print(f"Result: {result}")

if __name__ == '__main__':
    main()