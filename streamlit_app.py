import streamlit as st
import requests
from bs4 import BeautifulSoup
import re
import json
from backend.task_breakdown import break_down_task
from backend.summarization import summarize_content
from backend.question_generation import generate_quiz
from backend.chat_assistant import ask_question
import about_page

def apply_styles():
    st.markdown("""
    <style>
        .main-header {
            font-size: 2.5rem;
            margin-bottom: 1rem;
        }
        
        .section-header {
            font-size: 1.8rem;
            margin-top: 1.5rem;
            margin-bottom: 1rem;
        }
        
        .info-box {
            background-color: #f0f2f6;
            border-radius: 0.5rem;
            padding: 1rem;
            margin-bottom: 1rem;
        }
        
        .success-box {
            background-color: #d1e7dd;
            border-radius: 0.5rem;
            padding: 1rem;
            margin-bottom: 1rem;
        }
        
        .warning-box {
            background-color: #fff3cd;
            border-radius: 0.5rem;
            padding: 1rem;
            margin-bottom: 1rem;
        }
        
        .task-item {
            background-color: #f8f9fa;
            border-left: 4px solid #4b6fff;
            padding: 0.75rem;
            margin-bottom: 0.5rem;
            border-radius: 0 0.25rem 0.25rem 0;
        }
    </style>
    """, unsafe_allow_html=True)

def main_header(text):
    st.markdown(f'<h1 class="main-header">{text}</h1>', unsafe_allow_html=True)

def section_header(text):
    st.markdown(f'<h2 class="section-header">{text}</h2>', unsafe_allow_html=True)

def info_box(text):
    st.markdown(f'<div class="info-box">{text}</div>', unsafe_allow_html=True)

def success_box(text):
    st.markdown(f'<div class="success-box">{text}</div>', unsafe_allow_html=True)

def warning_box(text):
    st.markdown(f'<div class="warning-box">{text}</div>', unsafe_allow_html=True)

def task_item(text, idx=None):
    prefix = f"{idx}. " if idx is not None else ""
    st.markdown(f'<div class="task-item">{prefix}{text}</div>', unsafe_allow_html=True)

def is_valid_url(url):
    url_pattern = re.compile(
        r'^(https?:\/\/)?' 
        r'(www\.)?' 
        r'([a-zA-Z0-9-]+\.)+'
        r'[a-zA-Z]{2,}'
        r'(\/[a-zA-Z0-9-._~:/?#[\]@!$&\'()*+,;=]*)?' 
        r'$'
    )
    return bool(url_pattern.match(url))

def render_home_page():
    main_header("Welcome to TaskTamer")
    
    st.write("TaskTamer is your personal productivity assistant that helps you break down complex tasks, summarize information, and generate quizzes.")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Task Breakdown")
        st.write("Turn overwhelming tasks into manageable steps")
        if st.button("Try Task Breakdown", key="task_btn"):
            st.session_state["navigation"] = "Task Breakdown"
            st.experimental_rerun()
            
        st.subheader("Summarization")
        st.write("Extract key insights from text, web pages, or YouTube videos")
        if st.button("Try Summarization", key="summary_btn"):
            st.session_state["navigation"] = "Summarization"
            st.experimental_rerun()
            
    with col2:
        st.subheader("Quiz Generator")
        st.write("Create quizzes from your learning materials")
        if st.button("Try Quiz Generator", key="quiz_btn"):
            st.session_state["navigation"] = "Quiz Generator"
            st.experimental_rerun()
            
        st.subheader("Chat Assistant")
        st.write("Ask questions and get help using TaskTamer")
        if st.button("Try Chat Assistant", key="chat_btn"):
            st.session_state["navigation"] = "Chat"
            st.experimental_rerun()
    
    info_box("""
    <b>Getting Started:</b>
    <ol>
        <li>Select a feature from the sidebar</li>
        <li>Enter your task or content</li>
        <li>Get instant results!</li>
    </ol>
    """)

def render_task_page():
    main_header("Task Breakdown")
    
    with st.form(key="task_form"):
        task_description = st.text_area(
            "Enter a complex task you want to break down:", 
            height=150,
            help="Describe your task in detail for better results"
        )
        
        examples = st.expander("Show examples")
        with examples:
            st.write("• Write a research paper on AI ethics")
            st.write("• Create a personal budget plan for the next year")
            st.write("• Organize a virtual conference for 100+ attendees")
        
        submit_button = st.form_submit_button("Break Down Task")
    
    if submit_button:
        if not task_description:
            warning_box("Please enter a task description")
            return
            
        with st.spinner("Breaking down your task..."):
            steps = break_down_task(task_description)
            
        if steps:
            section_header("Here's your task breakdown:")
            
            for i, step in enumerate(steps, 1):
                task_item(step, i)
                
            st.download_button(
                label="Download Task Breakdown",
                data="\n".join([f"{i+1}. {step}" for i, step in enumerate(steps)]),
                file_name="task_breakdown.txt",
                mime="text/plain"
            )
        else:
            warning_box("Could not generate steps. Please try rewording your task.")

def render_summary_page():
    main_header("Content Summarizer")
    
    st.write("Summarize text, web pages, or YouTube videos")
    
    tab1, tab2 = st.tabs(["Text Input", "URL"])
    
    with tab1:
        text_content = st.text_area(
            "Enter the content you want to summarize:", 
            height=200,
            help="Paste the text you want to summarize"
        )
        
        if st.button("Summarize Text"):
            if not text_content:
                warning_box("Please enter some text to summarize")
                return
                
            with st.spinner("Generating summary..."):
                summary = summarize_content(content=text_content)
                
            if summary:
                section_header("Summary")
                st.write(summary)
                
                st.download_button(
                    label="Download Summary",
                    data=summary,
                    file_name="summary.txt",
                    mime="text/plain"
                )
            else:
                warning_box("Could not generate summary. Please try with different content.")
    
    with tab2:
        url = st.text_input(
            "Enter a webpage or YouTube URL:",
            help="Works with most websites and YouTube videos"
        )
        
        if st.button("Summarize URL"):
            if not url:
                warning_box("Please enter a URL")
                return
                
            if not is_valid_url(url):
                warning_box("Please enter a valid URL")
                return
                
            with st.spinner("Fetching content and generating summary..."):
                summary = summarize_content(url=url)
                
            if summary and not summary.startswith("Error"):
                section_header("Summary")
                st.write(summary)
                
                st.download_button(
                    label="Download Summary",
                    data=summary,
                    file_name="summary.txt",
                    mime="text/plain"
                )
            else:
                warning_box(f"Could not generate summary: {summary}")

def render_quiz_page():
    main_header("Quiz Generator")
    
    st.write("Create quizzes from text, web pages, or YouTube videos")
    
    tab1, tab2 = st.tabs(["Text Input", "URL"])
    
    with tab1:
        text_content = st.text_area(
            "Enter the content you want to create a quiz from:", 
            height=200,
            help="Paste the text you want to create a quiz from"
        )
        
        num_questions = st.slider("Number of questions", 1, 10, 3)
        
        if st.button("Generate Quiz", key="text_quiz_btn"):
            if not text_content:
                warning_box("Please enter some text to generate a quiz from")
                return
                
            with st.spinner("Generating quiz..."):
                quiz = generate_quiz(content=text_content, num_questions=num_questions)
                
            display_quiz(quiz)
    
    with tab2:
        url = st.text_input(
            "Enter a webpage or YouTube URL:",
            help="Works with most websites and YouTube videos"
        )
        
        num_questions = st.slider("Number of questions", 1, 10, 3, key="url_num_q")
        
        if st.button("Generate Quiz", key="url_quiz_btn"):
            if not url:
                warning_box("Please enter a URL")
                return
                
            if not is_valid_url(url):
                warning_box("Please enter a valid URL")
                return
                
            with st.spinner("Fetching content and generating quiz..."):
                quiz = generate_quiz(url=url, num_questions=num_questions)
                
            display_quiz(quiz)

def display_quiz(quiz_data):
    if not quiz_data:
        warning_box("Could not generate quiz. Please try with different content.")
        return
        
    section_header("Your Quiz")
    
    if "quiz_answers" not in st.session_state:
        st.session_state.quiz_answers = {}
        st.session_state.quiz_submitted = False
        st.session_state.quiz_score = 0
    
    for i, question in enumerate(quiz_data):
        st.subheader(f"Question {i+1}")
        st.write(question.get("question", ""))
        
        options = question.get("options", [])
        if options:
            answer_key = f"q_{i}"
            st.session_state.quiz_answers[answer_key] = question.get("answer", "")
            
            selected = st.radio(
                "Select your answer:",
                options,
                key=f"quiz_{i}"
            )
    
    if st.button("Submit Quiz"):
        st.session_state.quiz_submitted = True
        st.session_state.quiz_score = 0
        
        for i in range(len(quiz_data)):
            answer_key = f"q_{i}"
            selected = st.session_state[f"quiz_{i}"]
            
            if selected == st.session_state.quiz_answers[answer_key]:
                st.session_state.quiz_score += 1
        
        score_percentage = (st.session_state.quiz_score / len(quiz_data)) * 100
        success_box(f"Your score: {st.session_state.quiz_score}/{len(quiz_data)} ({score_percentage:.1f}%)")
        
        for i in range(len(quiz_data)):
            answer_key = f"q_{i}"
            selected = st.session_state[f"quiz_{i}"]
            correct = st.session_state.quiz_answers[answer_key]
            
            if selected == correct:
                st.success(f"Question {i+1}: Correct!")
            else:
                st.error(f"Question {i+1}: Incorrect. The correct answer is: {correct}")
    
    if st.button("Download Quiz"):
        quiz_json = json.dumps(quiz_data, indent=2)
        st.download_button(
            label="Download as JSON",
            data=quiz_json,
            file_name="quiz.json",
            mime="application/json"
        )

def render_chat_page():
    main_header("TaskTamer Assistant")
    
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []
    
    for message in st.session_state.chat_history:
        role = message["role"]
        content = message["content"]
        
        if role == "user":
            st.write(f"You: {content}")
        else:
            st.write(f"TaskTamer: {content}")
    
    question = st.text_input("Ask a question about TaskTamer or how to use its features:")
    
    if st.button("Ask"):
        if not question:
            warning_box("Please enter a question")
            return
            
        with st.spinner("Generating answer..."):
            answer = ask_question(question)
            
        st.session_state.chat_history.append({"role": "user", "content": question})
        st.session_state.chat_history.append({"role": "assistant", "content": answer})
        
        st.experimental_rerun()

def main():
    try:
        apply_styles()
        
        if "initialized" not in st.session_state:
            st.session_state.initialized = True
            st.session_state.navigation = "Home"
        
        st.sidebar.title("TaskTamer")
        
        pages = {
            "Home": render_home_page,
            "Task Breakdown": render_task_page,
            "Summarization": render_summary_page,
            "Quiz Generator": render_quiz_page,
            "Chat": render_chat_page,
            "About": about_page.render_about_page
        }
        
        selection = st.sidebar.radio("Navigate", list(pages.keys()))
        
        st.sidebar.markdown("---")
        st.sidebar.info("**TaskTamer** helps you manage complex tasks, summarize content, and test your knowledge.")
        
        current_page = pages.get(selection)
        if current_page:
            current_page()
        else:
            st.error("Page not found. Please select a valid page.")
            
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
        st.write("Please try again or contact support.")

if __name__ == "__main__":
    main()