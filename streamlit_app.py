import streamlit as st
import re
import json
import streamlit as st
from ui.pages.home_page import render_home_page
from ui.pages.task_page import render_task_page
from ui.pages.summary_page import render_summary_page
from ui.pages.quiz_pages import render_quiz_page
from ui.pages.chat_page import render_chat_page
from ui.pages.about_page import render_about_page
from ui.styles import apply_styles

APP_TITLE = "TaskTamer"
APP_DESCRIPTION = "**TaskTamer** helps you break down complex tasks, summarize content, and test your knowledge."
DEVELOPER_NAME = "Alessandra Batalha"


def apply_styles():
    st.markdown("""
    <style>
        /* Main color scheme from blue to purple gradient */
        :root {
            --blue-color: #1E88E5;
            --teal-color: #27C0AC;
            --green-color: #8FDB69;
            --purple-color: #9B4DCA;
            --light-purple-color: #D24CFF;
        }
        
        .main-header {
            font-size: 2.5rem;
            margin-bottom: 1.5rem;
            background: linear-gradient(90deg, var(--blue-color), var(--purple-color));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            font-weight: 700;
        }
        
        .section-header {
            font-size: 1.8rem;
            margin-top: 2rem;
            margin-bottom: 1rem;
            background: linear-gradient(90deg, var(--blue-color), var(--teal-color));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            font-weight: 600;
        }
        
        .info-box {
            background-color: #E3F2FD;
            border-left: 5px solid var(--blue-color);
            border-radius: 0.5rem;
            padding: 1.2rem;
            margin-bottom: 1.5rem;
        }
        
        .success-box {
            background-color: #E8F5E9;
            border-left: 5px solid var(--green-color);
            border-radius: 0.5rem;
            padding: 1.2rem;
            margin-bottom: 1.5rem;
        }
        
        .warning-box {
            background-color: #FFF8E1;
            border-left: 5px solid var(--teal-color);
            border-radius: 0.5rem;
            padding: 1.2rem;
            margin-bottom: 1.5rem;
        }
        
        .task-item {
            background-color: #FAFAFA;
            border-left: 4px solid var(--blue-color);
            padding: 1rem;
            margin-bottom: 0.8rem;
            border-radius: 0 0.5rem 0.5rem 0;
            font-size: 1.05rem;
        }
        
        /* Enhanced Task Breakdown Styles */
        .task-overview {
            background-color: #F3F6FF;
            border-radius: 0.8rem;
            padding: 1.5rem;
            margin-bottom: 1.5rem;
            border: 1px solid #E1E5F2;
        }
        
        .step-card {
            background: white;
            border-radius: 8px;
            padding: 16px;
            margin-bottom: 16px;
            box-shadow: 0 2px 5px rgba(0,0,0,0.05);
            border-left: 4px solid var(--blue-color);
        }
        
        .step-heading {
            font-weight: 600;
            font-size: 1.1rem;
            margin-bottom: 8px;
            color: #2C3E50;
        }
        
        .step-meta {
            display: flex;
            font-size: 0.9rem;
            color: #7F8C8D;
            margin-bottom: 12px;
        }
        
        .step-meta-item {
            margin-right: 16px;
        }
        
        .step-tip {
            background: #F8F9FA;
            padding: 10px;
            border-radius: 6px;
            font-size: 0.9rem;
            border-left: 3px solid var(--teal-color);
        }
        
        .step-high {
            border-left: 4px solid #FF5252;
        }
        
        .step-medium {
            border-left: 4px solid #FFC107;
        }
        
        .step-low {
            border-left: 4px solid #4CAF50;
        }
        
        .reward-card {
            background: linear-gradient(135deg, #E3F2FD, #F3E5F5);
            border-radius: 8px;
            padding: 16px;
            margin-top: 24px;
            border: 1px dashed var(--purple-color);
        }
        
        /* Stylize buttons */
        .stButton>button {
            background: linear-gradient(90deg, var(--blue-color), var(--purple-color));
            color: white;
            font-weight: 500;
            border: none;
            border-radius: 0.3rem;
            padding: 0.5rem 1rem;
            transition: all 0.3s ease;
        }
        
        .stButton>button:hover {
            background: linear-gradient(90deg, var(--purple-color), var(--blue-color));
            transform: translateY(-2px);
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        }
        
        /* Tabs styling */
        .stTabs [data-baseweb="tab-list"] {
            gap: 2px;
        }
        
        .stTabs [data-baseweb="tab"] {
            background-color: #F3F4F6;
            padding: 10px 20px;
            border-radius: 4px 4px 0 0;
        }
        
        .stTabs [aria-selected="true"] {
            background: linear-gradient(90deg, var(--blue-color), var(--teal-color));
            color: white;
        }
                /* Chat message styling */
        .user-message {
            background-color: #F0F4FF;
            padding: 12px;
            border-radius: 10px 10px 0 10px;
            margin: 10px 0;
            align-self: flex-end;
            max-width: 80%;
        }
        
        .assistant-message {
            background: linear-gradient(135deg, #E2F0FF, #F2E7FF);
            padding: 12px;
            border-radius: 10px 10px 10px 0;
            margin: 10px 0;
            align-self: flex-start;
            max-width: 80%;
        }
        
        /* Logo styling */
        .logo-text {
            font-size: 2rem;
            font-weight: 800;
            letter-spacing: 1px;
            background: linear-gradient(90deg, var(--blue-color), var(--light-purple-color));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }
        
        .getting-things-done {
            font-size: 0.9rem;
            color: var(--green-color);
            font-weight: 500;
            margin-left: 10px;
        }
        
        /* Quiz styling */
        .quiz-question {
            background-color: #F8F9FA;
            padding: 15px;
            border-radius: 8px;
            margin-bottom: 20px;
            border-left: 4px solid var(--blue-color);
        }
        
        .correct-answer {
            background-color: #E8F5E9;
            padding: 10px;
            border-radius: 4px;
            border-left: 4px solid var(--green-color);
        }
        
        .incorrect-answer {
            background-color: #FFEBEE;
            padding: 10px;
            border-radius: 4px;
            border-left: 4px solid #F44336;
        }
    </style>
    """, unsafe_allow_html=True)

def initialize_session_state():
    
    if "initialized" not in st.session_state:
        st.session_state.initialized = True
        st.session_state.task_data = {}
        st.session_state.quiz_history = []
        st.session_state.chat_history = []

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

def logo_header():
    st.markdown(
        '<div style="display: flex; align-items: center;">'
        '<span class="logo-text">TASK TAMER</span>'
        '<span class="getting-things-done">GETTING THINGS DONE</span>'
        '</div>', 
        unsafe_allow_html=True
    )

def render_step_card(step):
    priority_class = f"step-{step['priority'].lower()}" if 'priority' in step else ""
    
    st.markdown(f'<div class="step-card {priority_class}">', unsafe_allow_html=True)
    st.markdown(f'<div class="step-heading">Step {step["number"]}: {step["description"]}</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="step-meta">', unsafe_allow_html=True)
    if 'time' in step:
        st.markdown(f'<div class="step-meta-item">⏱️ Time: {step["time"]} min</div>', unsafe_allow_html=True)
    if 'priority' in step:
        st.markdown(f'<div class="step-meta-item">🔍 Priority: {step["priority"]}</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    if 'adhd_tip' in step:
        st.markdown(f'<div class="step-tip">💡 ADHD Tip: {step["adhd_tip"]}</div>', unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)


def is_valid_url(url):
    url_pattern = re.compile(r'^(https?:\/\/)?(www\.)?([a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}(\/[a-zA-Z0-9-._~:/?#[\]@!$&\'()*+,;=]*)?$')
    return bool(url_pattern.match(url))


def render_home_page():
    logo_header()
    
    st.write("Your personal productivity assistant that helps you break down complex tasks, summarize information, and generate quizzes.")
    
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("🧩 Task Breakdown")
        st.write("Turn overwhelming tasks into manageable steps")
            
        st.subheader("📝 Summarization")
        st.write("Extract key insights from text and web pages")
    
    with col2:
        st.subheader("🧠 Quiz Generator")
        st.write("Create quizzes from your learning materials")
        
        st.subheader("🤖 Otto - Your Assistant")
        st.write("Ask questions and get help anytime")
    
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
    
    
    with st.expander("Customize your task breakdown"):
        detail_level = st.radio(
            "Level of detail",
            ["basic", "standard", "comprehensive"],
            index=1,
            help="Choose how detailed your task breakdown should be."
        )
        
        
        st.write("These options help make your task breakdown more personalized to your needs.")
        adhd_support = st.checkbox("Include ADHD-friendly tips", value=True, 
                                  help="Add specific strategies to help maintain focus and motivation")
        
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
            st.write("• Design a marketing campaign for a new product")
            st.write("• Plan a website redesign project")
        
        submit_button = st.form_submit_button("Break Down Task")
    
    if submit_button:
        if not task_description:
            warning_box("Please enter a task description")
            return
            
        with st.spinner("Breaking down your task..."):
            
            task_breaker = TaskBreakdown(detail_level)
            result = task_breaker.break_task(task_description)
            
        if result and "steps" in result and result["steps"]:
            
            st.markdown(f'<div class="task-overview">', unsafe_allow_html=True)
            st.markdown(f"<h3>{result['task']}</h3>", unsafe_allow_html=True)
            st.write(result["overview"])
            st.markdown('</div>', unsafe_allow_html=True)
            
            section_header("Step-by-Step Breakdown")
            
            for step in result["steps"]:
                render_step_card(step)
                
            
            if result["reward_suggestion"]:
                st.markdown(f'<div class="reward-card">🎉 <strong>Reward Suggestion:</strong> {result["reward_suggestion"]}</div>', unsafe_allow_html=True)
                
           
            col1, col2 = st.columns(2)
            with col1:
               
                simple_steps = "\n".join([f"{i+1}. {step['description']}" for i, step in enumerate(result["steps"])])
                st.download_button(
                    label="Download Simple Steps",
                    data=simple_steps,
                    file_name="task_breakdown.txt",
                    mime="text/plain"
                )
            
            with col2:
                
                st.download_button(
                    label="Download Full Breakdown",
                    data=json.dumps(result, indent=2),
                    file_name="task_breakdown.json",
                    mime="application/json"
                )
        else:
            warning_box("Could not generate steps. Please try rewording your task.")

def render_summary_page():
    main_header("Content Summarizer")
    
    st.write("Summarize text or web pages to extract key insights quickly.")
    
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
            "Enter a webpage URL:",
            help="Works with most websites"
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
        st.markdown(f'<div class="quiz-question">', unsafe_allow_html=True)
        st.subheader(f"Question {i+1}")
        st.write(question.get("question", ""))
        
        options = question.get("options", [])
        if options:
            answer_key = f"q_{i}"
            st.session_state.quiz_answers[answer_key] = question.get("answer", "")
            
            st.radio(
                "Select your answer:",
                options,
                key=f"quiz_{i}"
            )
        st.markdown('</div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        submit_button = st.button("Submit Quiz")
    
    with col2:
        download_button = st.button("Download Quiz")
    
    if submit_button:
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
                st.markdown(f'<div class="correct-answer">Question {i+1}: ✓ Correct!</div>', unsafe_allow_html=True)
            else:
                st.markdown(f'<div class="incorrect-answer">Question {i+1}: ✗ Incorrect. The correct answer is: {correct}</div>', unsafe_allow_html=True)
    
    if download_button:
        quiz_json = json.dumps(quiz_data, indent=2)
        st.download_button(
            label="Download as JSON",
            data=quiz_json,
            file_name="quiz.json",
            mime="application/json"
        )

def render_quiz_page():
    main_header("Quiz Generator")
    
    st.write("Create interactive quizzes from text or web pages to test your knowledge.")
    
    tab1, tab2 = st.tabs(["Text Input", "URL"])
    
    with tab1:
        text_content = st.text_area(
            "Enter the content you want to create a quiz from:", 
            height=200,
            help="Paste the text you want to create a quiz from"
        )
        
        num_questions = st.slider("Number of questions", 1, 8, 3)
        
        if st.button("Generate Quiz", key="text_quiz_btn"):
            if not text_content:
                warning_box("Please enter some text to generate a quiz from")
                return
                
            with st.spinner("Generating quiz..."):
                quiz = generate_quiz(content=text_content, num_questions=num_questions)
                
            display_quiz(quiz)
    
    with tab2:
        url = st.text_input(
            "Enter a webpage URL:",
            help="Works with most websites"
        )
        
        num_questions = st.slider("Number of questions", 1, 8, 3, key="url_num_q")
        
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

def render_chat_page():
    main_header("Otto - Your TaskTamer Assistant")
    
    st.write("Hi, I'm Otto! I can help you with task management, summarization, and quiz generation. Ask me anything about using TaskTamer or how to be more productive!")
    
    
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []
    
    
    for message in st.session_state.chat_history:
        role = message["role"]
        content = message["content"]
        
        if role == "user":
            st.markdown(f'<div class="user-message"><strong>You:</strong> {content}</div>', unsafe_allow_html=True)
        else:
            st.markdown(f'<div class="assistant-message"><strong>Otto:</strong> {content}</div>', unsafe_allow_html=True)
    
   
    with st.form(key="chat_form"):
        question = st.text_input("Ask Otto a question:")
        submit_button = st.form_submit_button("Send")
    
    if submit_button:
        if not question:
            warning_box("Please enter a question")
            return
            
        
        st.session_state.chat_history.append({"role": "user", "content": question})
        
      
        with st.spinner("Otto is thinking..."):
            answer = ask_question(question)
            
        
        st.session_state.chat_history.append({"role": "assistant", "content": answer})
        
        
        st.experimental_rerun()
        
    
    if st.session_state.chat_history:
        if st.button("Clear Chat"):
            st.session_state.chat_history = []
            st.experimental_rerun()

def render_about_page():
    main_header("About TaskTamer")
    
    st.write("""
    TaskTamer is a productivity tool designed to help users manage their learning and workflow more effectively. 
    The application combines several powerful features to break down complex tasks, summarize content, and generate 
    quizzes for better knowledge retention.
    """)
    
    section_header("Key Features")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### 🧩 Task Breakdown")
        st.write("Convert complex tasks into manageable, actionable steps")
        
        st.markdown("#### 📝 Content Summarization")
        st.write("Extract key insights from text and web pages")
    
    with col2:
        st.markdown("#### 🧠 Quiz Generation")
        st.write("Create interactive quizzes from any content to test your knowledge")
        
        st.markdown("#### 🤖 Otto - Your Assistant")
        st.write("Get help and answers to your productivity questions")
    
    section_header("How TaskTamer Helps You")
    
    st.write("""
    TaskTamer was created with a focus on helping students and professionals, particularly those with ADHD or who struggle 
    with information overload. By breaking complex tasks into manageable steps, extracting key information, and providing 
    interactive learning tools, TaskTamer helps users:
    
    - **Reduce overwhelm** by transforming large projects into clear, actionable steps
    - **Improve focus** by identifying the most important information in any content
    - **Enhance learning** through interactive quizzes that reinforce knowledge
    - **Save time** by quickly summarizing long articles or web pages
    """)
    
    section_header("Technology")
    
    st.write("""
    TaskTamer leverages natural language processing techniques to analyze content and provide intelligent assistance.
    The application is built with:
    
    - **Streamlit** for the interactive user interface
    - **BeautifulSoup** for web content extraction
    - **Custom NLP algorithms** for text analysis and processing
    """)
    
    section_header("About the Developer")
    
    st.write("""
    TaskTamer was created by **Alessandra Batalha** as part of her final year project at Dublin Business School. 
    The project represents the culmination of her studies in Computer Science, combining practical software 
    engineering skills with artificial intelligence techniques.
    
    Alessandra developed TaskTamer with a focus on helping students and professionals manage their learning and 
    work tasks more efficiently. The project demonstrates her skills in full-stack development and user experience design.
    """)
    
    info_box("""
    <b>Contact:</b><br>
    For more information about this project or to provide feedback, please contact Alessandra Batalha via Dublin Business School.
    """)

def main():
    try:
        
        apply_styles()
        
        
        if "initialized" not in st.session_state:
            st.session_state.initialized = True
            st.session_state.task_data = {}
            st.session_state.quiz_history = []
            st.session_state.chat_history = []
        
        
        st.sidebar.title("TaskTamer")
        st.sidebar.markdown("Your productivity assistant")
        st.sidebar.markdown("---")
        
        pages = {
            "Home": render_home_page,
            "Task Breakdown": render_task_page,
            "Summarization": render_summary_page,
            "Quiz Generator": render_quiz_page,
            "Otto Assistant": render_chat_page,
            "About": render_about_page
        }
        
        selection = st.sidebar.radio("Navigate", list(pages.keys()), index=0)
        
        st.sidebar.markdown("---")
        st.sidebar.info(f"{APP_DESCRIPTION}\n\nMade with ❤️ by {DEVELOPER_NAME}")
        
        
        pages[selection]()
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
        st.write("Please try again or contact support.")

if __name__ == "__main__":
    main()