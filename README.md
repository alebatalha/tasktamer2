# TaskTamer 🐙

TaskTamer is a productivity tool designed to help users manage their learning and workflow more effectively. The application combines several powerful features to break down complex tasks, summarize content, and generate quizzes for better knowledge retention - all with the help of Otto, your eight-tentacled productivity assistant!

## Live Demo

Check out the live application: [TaskTamer](https://tasktamer2-2vvlazxfwprjowe6jty7cu.streamlit.app/)

**Direct Link**: https://tasktamer2-2vvlazxfwprjowe6jty7cu.streamlit.app/

## Features

### 🧩 Task Breakdown
Convert complex tasks into manageable, actionable steps with time estimates, priority levels, and ADHD-friendly tips.

### 📝 Summarization
Extract key insights from text, web pages, and YouTube videos with customizable summary formats.

### 🧠 Quiz Generator
Create interactive quizzes from any content to test your knowledge, with customizable number of questions.

### 🐙 Otto - Your Assistant
Get help and answers to your productivity questions from Otto, your friendly octopus assistant.

## Why TaskTamer Was Created

TaskTamer was created specifically to assist learners, primarily those with ADHD, through educational and task management features. The tool addresses common challenges faced by students with attention difficulties:

- **Information Overload**: Summarizing helps condense large amounts of information into digestible chunks
- **Task Organization**: Breaking down complex tasks makes them less overwhelming
- **Knowledge Retention**: Quiz generation reinforces learning through active recall
- **Accessibility**: Simple interface designed for all cognitive styles

The vision was to develop a virtual assistant that adapts to students' requirements by offering personalized recommendations and improved accessibility, making learning more inclusive.

## Meet Otto - Your Eight-Tentacled Assistant

Otto is your friendly octopus productivity assistant! Just like real octopuses are known for their intelligence and problem-solving abilities, Otto is designed to help you tackle complex challenges with creative solutions.

With eight helpful tentacles, Otto can:
- Break down complex tasks into manageable steps
- Extract key information from lengthy content
- Create engaging quizzes to test your knowledge
- Provide personalized productivity advice
- Offer ADHD-friendly strategies for maintaining focus and motivation
- Share tips for overcoming procrastination and managing your time effectively

## Installation

1. Clone the repository:
```bash
git clone https://github.com/alebatalha/tasktamer.git
cd tasktamer
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Install optional dependencies for additional functionality:
```bash
pip install poppler-utils python-magic youtube-transcript-api
```

## Usage

Run the Streamlit app:
```bash
streamlit run streamlit_app.py
```

The application will be available at http://localhost:8501

## Project Structure

```
tasktamer/
├── backend/             # Backend logic
│   ├── __init__.py
│   ├── chat_assistant.py    # Otto assistant implementation
│   ├── question_generation.py # Quiz generation
│   ├── summarization.py     # Text summarization
│   └── task_breakdown.py    # Task breakdown logic
├── ui/                  # UI components
│   └── pages/
│       └── about_page.py    # About page information
├── utils/               # Utility functions
├── streamlit_app.py     # Main application
└── requirements.txt     # Project dependencies
```

## Technologies Used

- **Streamlit**: For the interactive user interface
- **BeautifulSoup**: For web content extraction
- **NLTK (optional)**: For advanced text processing
- **Requests**: For fetching web content
- **Python**: Core programming language

## Key Features in Detail

### Task Breakdown
- Convert overwhelming tasks into clear, manageable steps
- Each step includes helpful emojis and information
- Easily downloadable task breakdowns
- Specialized templates for different task types (research, presentations, project management, etc.)

### Summarization
- Extract key information from text and web content
- Support for summarizing web pages via URL
- Clean, distraction-free summaries
- Downloadable for later reference

### Quiz Generator
- Create interactive quizzes from any content
- Customizable number of questions
- Immediate feedback on quiz performance
- Download quizzes for future study sessions

### Otto Assistant
- Friendly, accessible interface with Otto the Octopus
- Quick answers to productivity questions
- ADHD-friendly tips and strategies
- Guidance on using all TaskTamer features

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Author

Created by **Alessandra Batalha** as part of her final year project at Dublin Business School.

GitHub: [@alebatalha](https://github.com/alebatalha)

---

Made with 🐙 and ❤️
