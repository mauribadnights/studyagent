# PDF Question Generator & Quiz System

A Python tool that generates questions from PDF documents using LLMs and conducts interactive quizzes with score tracking.

## Features

- 📄 Generate MCQ, short answer, and long answer questions from PDFs
- 📊 Interactive quiz session with automatic answer evaluation
- 🏆 Track scores per question (correct/partial/wrong)
- 📂 Organized storage of generated questions
- 🔍 Supports multiple question types per document
- 🤖 Uses GPT-3.5-turbo for question generation and evaluation

## Installation

1. Clone repository:
```bash
git clone https://github.com/yourusername/pdf-quiz-generator.git
cd pdf-quiz-generator
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Create `.env` file with your OpenAI API key:
```ini
OPENAI_API_KEY=your_api_key_here
```

## Usage

```bash
python qa_generator.py path/to/document.pdf [options]
```

### Options:
- `-n NUM`, `--num_questions NUM`: Questions per type (default: 3)
- `-t TYPES`, `--types TYPES`: Question types (space-separated: mcq short long)

### Example:
```bash
python qa_generator.py example.pdf -n 5 -t mcq short
```

### Quiz Session Flow:
1. Questions are presented by type
2. Free-text answers for short/long questions
3. Immediate feedback with correctness evaluation
4. Scores automatically saved in `scores_{filename}.json`

## Repository Structure

```
.
├── qa_generator.py          # Main entry point
├── utils/                   # Helper modules
│   ├── pdf_reader.py        # PDF text extraction
│   ├── llm_handler.py       # OpenAI interactions
│   └── file_manager.py      # Question/scores storage
├── questions/               # Generated questions storage
├── scores_example.pdf.json  # Example score file
├── example.pdf              # Sample document
└── .env                     # API configuration
```

## Configuration

Edit `.env` file:
```ini
OPENAI_API_KEY=your_api_key_here
```

## Score Tracking

Scores are stored in JSON format tracking:
- Total correct answers
- Partially correct responses
- Incorrect attempts

Example score entry:
```json
{
  "a1b2c3...": {
    "correct": 2,
    "partial": 1,
    "wrong": 0
  }
}
```

## Limitations

- Requires OpenAI API access (costs may apply)
- PDF text extraction quality depends on document structure
- Evaluation accuracy varies with LLM performance

## Roadmap

- [ ] Add local LLM support (e.g., HuggingFace)
- [ ] Implement web-based UI
- [ ] Add question difficulty levels
- [ ] Support image-based PDFs
- [ ] Export quizzes to JSON/CSV


# License
tbd