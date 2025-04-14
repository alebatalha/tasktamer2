import streamlit as st
import requests
from bs4 import BeautifulSoup
import re
import json
import random
from backend.task_breakdown import break_down_task
from backend.summarization import summarize_content
from backend.question_generation import generate_quiz
from backend.chat_assistant import ask_question
import about_page

st.set_page_config(
    page_title="TaskTamer",
    page_icon="🐙",
    layout="wide",
    initial_sidebar_state="expanded",
)

def apply_styles():
    st.markdown("""
    <style>
        /* Main color scheme - octopus theme with gradients */
        :root {
            --blue-color: #1E88E5;
            --teal-color: #00BCD4;
            --purple-color: #9C27B0;
            --green-color: #4CAF50;
            --pink-color: #FF4081;
        }
        
        .main-header {
            font-size: 2.5rem;
            margin-bottom: 1.5rem;
            background: linear-gradient(90deg, var(--teal-color), var(--purple-color));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            font-weight: 700;
        }
        
        .section-header {
            font-size: 1.8rem;
            margin-top: 1.5rem;
            margin-bottom: 1rem;
            background: linear-gradient(90deg, var(--blue-color), var(--teal-color));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            font-weight: 600;
        }
        
        .info-box {
            background-color: rgba(0, 188, 212, 0.1);
            border-left: 5px solid var(--teal-color);
            border-radius: 0.5rem;
            padding: 1.2rem;
            margin-bottom: 1.5rem;
            box-shadow: 0 2px 5px rgba(0,0,0,0.05);
        }
        
        .success-box {
            background-color: rgba(76, 175, 80, 0.1);
            border-left: 5px solid var(--green-color);
            border-radius: 0.5rem;
            padding: 1.2rem;
            margin-bottom: 1.5rem;
            box-shadow: 0 2px 5px rgba(0,0,0,0.05);
        }
        
        .warning-box {
            background-color: rgba(255, 152, 0, 0.1);
            border-left: 5px solid #FF9800;
            border-radius: 0.5rem;
            padding: 1.2rem;
            margin-bottom: 1.5rem;
            box-shadow: 0 2px 5px rgba(0,0,0,0.05);
        }
        
        .task-item {
            background-color: white;
            border-left: 4px solid var(--blue-color);
            padding: 15px;
            margin-bottom: 12px;
            border-radius: 8px;
            box-shadow: 0 2px 5px rgba(0,0,0,0.05);
            transition: transform 0.2s ease, box-shadow 0.2s ease;
        }
        
        .task-item:hover {
            transform: translateY(-2px);
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        }
        
        /* Improved chat bubbles */
        .user-message {
            background: linear-gradient(135deg, #E3F2FD, #BBDEFB);
            padding: 15px;
            border-radius: 18px 18px 0 18px;
            margin: 15px 0;
            max-width: 85%;
            margin-left: auto;
            box-shadow: 0 2px 5px rgba(0,0,0,0.05);
        }
        
        .assistant-message {
            background: linear-gradient(135deg, #E1F5FE, #B3E5FC);
            padding: 15px;
            border-radius: 18px 18px 18px 0;
            margin: 15px 0;
            max-width: 85%;
            margin-right: auto;
            box-shadow: 0 2px 5px rgba(0,0,0,0.05);
            position: relative;
        }
        
        /* Octopus icon before assistant messages */
        .assistant-message::before {
            content: "🐙";
            position: absolute;
            left: -25px;
            top: 10px;
            font-size: 20px;
        }
        
        /* Enhanced buttons */
        .stButton > button {
            background: linear-gradient(90deg, var(--teal-color), var(--blue-color));
            color: white;
            border: none;
            border-radius: 25px;
            padding: 8px 16px;
            font-weight: 500;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
            transition: all 0.3s ease;
        }
        
        .stButton > button:hover {
            background: linear-gradient(90deg, var(--blue-color), var(--purple-color));
            box-shadow: 0 5px 15px rgba(0,0,0,0.15);
            transform: translateY(-2px);
        }
        
        /* Quiz styling */
        .quiz-question {
            background-color: rgba(30, 136, 229, 0.06);
            padding: 20px;
            border-radius: 12px;
            margin-bottom: 25px;
            border-left: 5px solid var(--blue-color);
            box-shadow: 0 3px 10px rgba(0,0,0,0.04);
        }
        
        /* Logo styling */
        .logo-text {
            font-size: 2.2rem;
            font-weight: 800;
            letter-spacing: 1px;
            background: linear-gradient(90deg, var(--teal-color), var(--purple-color));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 5px;
        }
        
        .logo-tagline {
            font-size: 0.9rem;
            color: #4CAF50;
            font-weight: 500;
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
        
    st.write("Your personal productivity assistant with eight tentacles ready to help you break down complex tasks, summarize information, and generate quizzes!")
    
    col1, col2 = st.columns(2)
    
    # Function to handle navigation
    def button_click(destination):
        st.session_state.navigation = destination
    
    with col1:
        st.subheader("🧩 Task Breakdown")
        st.write("Turn overwhelming tasks into manageable steps")
        st.button("Try Task Breakdown", 
                 key="task_btn", 
                 on_click=button_click,
                 args=("Task Breakdown",))
            
        st.subheader("📝 Summarization")
        st.write("Extract key insights from text and web pages")
        st.button("Try Summarization", 
                 key="summary_btn", 
                 on_click=button_click,
                 args=("Summarization",))
            
    with col2:
        st.subheader("🧠 Quiz Generator")
        st.write("Create quizzes from your learning materials")
        st.button("Try Quiz Generator", 
                 key="quiz_btn", 
                 on_click=button_click,
                 args=("Quiz Generator",))
            
        st.subheader("🐙 Otto - Your Assistant")
        st.write("Ask questions and get help anytime")
        st.button("Ask Otto", 
                 key="otto_btn", 
                 on_click=button_click,
                 args=("Chat",))
    
    info_box("""
    <b>Getting Started with TaskTamer:</b>
    <ol>
        <li>🧭 Select a feature from the sidebar</li>
        <li>✍️ Enter your task or content</li>
        <li>✨ Get instant results backed by octopus intelligence!</li>
    </ol>
    """)
    
    st.markdown("---")
    st.subheader("✨ How TaskTamer Helps You")
    
    with st.expander("🧩 Task Breakdown - Conquer large projects"):
        st.write("""
        Breaking down large, complex tasks into manageable steps helps reduce overwhelm and makes progress easier to track.
        TaskTamer analyzes your task description and creates a personalized, step-by-step plan that's easy to follow.
        
        Features:
        - 📊 Different detail levels to match your needs
        - 🧠 ADHD-friendly tips included with each step
        - ⏱️ Time estimates and priority levels
        - 📥 Downloadable action plans
        """)
        
    with st.expander("📝 Summarization - Extract key insights"):
        st.write("""
        Information overload is a common productivity killer. TaskTamer's summarization feature helps you quickly extract
        the most important points from any text, saving you time and improving comprehension.
        
        Features:
        - 📚 Summarize long articles or documents
        - 🌐 Process text from websites
        - 📱 Access summaries anywhere
        - 📥 Download summaries for later reference
        """)
        
    with st.expander("🧠 Quiz Generator - Test your knowledge"):
        st.write("""
        Active recall is one of the most effective study techniques. TaskTamer turns your content into interactive quizzes
        that help you reinforce learning and identify knowledge gaps.
        
        Features:
        - ❓ Create quizzes from any text
        - 🔢 Customizable number of questions
        - 📊 Track your performance
        - 🎯 Test your understanding
        """)
        
    with st.expander("🐙 Otto Assistant - Get personalized help"):
        st.write("""
        Otto is your friendly octopus assistant, ready to answer questions and provide guidance on using TaskTamer
        or improving your productivity in general.
        
        Features:
        - 💬 Get help with using TaskTamer features
        - 🧠 Ask about productivity techniques
        - 🎯 Get personalized advice for focus and time management
        - 💪 Tips for managing ADHD and overcoming procrastination
        """)
    
    productivity_tips = [
        "Break large tasks into smaller, manageable steps to reduce overwhelm.",
        "Use the Pomodoro Technique: 25 minutes of focused work followed by a 5-minute break.",
        "Plan your most challenging tasks during your peak energy hours.",
        "Create a dedicated workspace to signal to your brain that it's time to focus.",
        "Use the 2-minute rule: If a task takes less than 2 minutes, do it immediately.",
        "Try body doubling - working alongside someone else can boost accountability.",
        "Set specific, measurable goals rather than vague intentions.",
        "Schedule buffer time between tasks to account for transitions and unexpected issues.",
        "Use visual timers to make time more concrete and create urgency.",
        "Prioritize using the Eisenhower Matrix: Important/Urgent, Important/Not Urgent, etc."
    ]
    
    
    tip = random.choice(productivity_tips)
    tip_emojis = ["💡", "✨", "🌟", "⚡", "🚀", "🔑", "💪", "🧠"]
    
    st.markdown("---")
    st.markdown(f"### {random.choice(tip_emojis)} Productivity Tip of the Day")
    st.markdown(f"*\"{tip}\"*")

def render_task_page():
    main_header("🧩 Task Breakdown")
    
    st.write("Turn overwhelming projects into clear, manageable steps with Otto's eight-tentacled approach!")
    
    with st.expander("🎛️ Customize your task breakdown"):
        detail_level = st.radio(
            "Level of detail",
            ["basic", "standard", "comprehensive"],
            index=1,
            help="Choose how detailed your task breakdown should be."
        )
        
    with st.form(key="task_form"):
        task_description = st.text_area(
            "Enter a complex task you want to break down:", 
            height=150,
            help="Describe your task in detail for better results"
        )
        
        examples = st.expander("📋 Show examples")
        with examples:
            st.write("• 📝 Write a research paper on AI ethics")
            st.write("• 💰 Create a personal budget plan for the next year")
            st.write("• 🎪 Organize a virtual conference for 100+ attendees")
            st.write("• 📣 Design a marketing campaign for a new product")
            st.write("• 🖥️ Plan a website redesign project")
        
        submit_button = st.form_submit_button("Break Down Task")
    
    if submit_button:
        if not task_description:
            warning_box("Please enter a task description")
            return
            
        with st.spinner("🐙 Otto is breaking down your task..."):
            steps = break_down_task(task_description)
            
        if steps:
            section_header("Here's your task breakdown:")
            
            for i, step in enumerate(steps, 1):
                
                emoji_map = {
                    "define": "🎯", "create": "✨", "gather": "📚", "research": "🔍",
                    "identify": "👁️", "plan": "📋", "design": "🎨", "write": "✍️",
                    "organize": "🗂️", "review": "🔄", "test": "✅", "finalize": "🏁",
                    "track": "📊", "set": "⚙️", "list": "📝", "break": "🧩"
                }
                
                
                first_word = step.split()[0].lower()
                emoji = emoji_map.get(first_word, "✨")
                
                
                enhanced_step = f"{emoji} {step}"
                task_item(enhanced_step, i)
                
            success_box("🐙 Otto has broken down your task successfully! Remember to tackle one step at a time.")
                
            st.download_button(
                label="📥 Download Task Breakdown",
                data="\n".join([f"{i+1}. {step}" for i, step in enumerate(steps)]),
                file_name="task_breakdown.txt",
                mime="text/plain"
            )
        else:
            warning_box("Could not generate steps. Please try rewording your task.")

def render_summary_page():
    main_header("📝 Content Summarizer")
    
    st.write("Otto will help you extract the key insights from any text - like an octopus finding pearls in the ocean!")
    
    tab1, tab2 = st.tabs(["Text Input", "URL"])
    
    with tab1:
        text_content = st.text_area(
            "Enter the content you want to summarize:", 
            height=200,
            help="Paste the text you want to summarize"
        )
        
        if st.button("🐙 Summarize Text"):
            if not text_content:
                warning_box("Please enter some text to summarize")
                return
                
            with st.spinner("Otto is analyzing your text with all eight tentacles..."):
                summary = summarize_content(content=text_content)
                
            if summary:
                section_header("Your Summary")
                st.write(f"📝 {summary}")
                
                st.download_button(
                    label="📥 Download Summary",
                    data=summary,
                    file_name="summary.txt",
                    mime="text/plain"
                )
                
                success_box("🐙 Summary complete! Otto has extracted the key points with octopus precision!")
            else:
                warning_box("Could not generate summary. Please try with different content.")
    
    with tab2:
        url = st.text_input(
            "Enter a webpage URL:",
            help="Works with most websites"
        )
        
        if st.button("🐙 Summarize URL"):
            if not url:
                warning_box("Please enter a URL")
                return
                
            if not is_valid_url(url):
                warning_box("Please enter a valid URL")
                return
                
            with st.spinner("Otto is swimming through the web to fetch and analyze content..."):
                summary = summarize_content(url=url)
                
            if summary and not summary.startswith("Error"):
                section_header("Your Summary")
                st.write(f"🌐 {summary}")
                
                st.download_button(
                    label="📥 Download Summary",
                    data=summary,
                    file_name="summary.txt",
                    mime="text/plain"
                )
                
                success_box("🐙 Web content summarized! Otto has extracted the key information from the depths of the internet!")
            else:
                warning_box(f"Could not generate summary: {summary}")

def render_quiz_page():
    main_header("🧠 Quiz Generator")
    
    st.write("Otto will create interactive quizzes to test your knowledge - exercising your brain is as important as exercising Otto's tentacles!")
    
    tab1, tab2 = st.tabs(["Text Input", "URL"])
    
    with tab1:
        text_content = st.text_area(
            "Enter the content you want to create a quiz from:", 
            height=200,
            help="Paste the text you want to create a quiz from"
        )
        
        num_questions = st.slider("Number of questions", 1, 5, 3)
        
        if st.button("🐙 Generate Quiz", key="text_quiz_btn"):
            if not text_content:
                warning_box("Please enter some text to generate a quiz from")
                return
                
            with st.spinner("Otto is crafting questions with all eight brainy tentacles..."):
                quiz = generate_quiz(content=text_content, num_questions=num_questions)
                
            display_quiz(quiz)
    
    with tab2:
        url = st.text_input(
            "Enter a webpage URL:",
            help="Works with most websites"
        )
        
        num_questions = st.slider("Number of questions", 1, 5, 3, key="url_num_q")
        
        if st.button("🐙 Generate Quiz", key="url_quiz_btn"):
            if not url:
                warning_box("Please enter a URL")
                return
                
            if not is_valid_url(url):
                warning_box("Please enter a valid URL")
                return
                
            with st.spinner("Otto is diving into the website to create quiz questions..."):
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
        st.markdown(f'<div class="quiz-question">', unsafe_allow_html=True)
        st.subheader(f"Question {i+1}")
        question_text = question.get("question", "")
       
        if not question_text.startswith("🧠"):
            question_text = f"🧠 {question_text}"
        st.write(question_text)
        
        options = question.get("options", [])
        if options:
            answer_key = f"q_{i}"
            st.session_state.quiz_answers[answer_key] = question.get("answer", "")
            
            st.radio(
                "Select your answer:",
                options,
                key=f"quiz_{i}"
            )
        else:
            st.write("No answer options available.")
        st.markdown('</div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        submit_button = st.button("🧠 Submit Quiz")
    
    with col2:
        download_button = st.button("📥 Download Quiz")
    
    if submit_button:
        st.session_state.quiz_submitted = True
        st.session_state.quiz_score = 0
        
        for i in range(len(quiz_data)):
            answer_key = f"q_{i}"
            selected = st.session_state.get(f"quiz_{i}", "")
            correct = st.session_state.quiz_answers.get(answer_key, "")
            
            if selected and selected == correct:
                st.session_state.quiz_score += 1
        
        score_percentage = (st.session_state.quiz_score / len(quiz_data)) * 100 if quiz_data else 0
        
        
        if score_percentage >= 80:
            octopus_reaction = "🐙 Incredible job! Otto is impressed with your knowledge!"
        elif score_percentage >= 60:
            octopus_reaction = "🐙 Good work! Otto thinks you're swimming along nicely!"
        elif score_percentage >= 40:
            octopus_reaction = "🐙 Not bad! Otto suggests a little more practice!"
        else:
            octopus_reaction = "🐙 Otto believes in you! Let's review the material and try again!"
            
        success_box(f"{octopus_reaction}<br>Your score: {st.session_state.quiz_score}/{len(quiz_data)} ({score_percentage:.1f}%)")
        
        for i in range(len(quiz_data)):
            answer_key = f"q_{i}"
            selected = st.session_state.get(f"quiz_{i}", "")
            correct = st.session_state.quiz_answers.get(answer_key, "")
            
            if selected and selected == correct:
                st.markdown(f'<div style="background-color: #E8F5E9; padding: 10px; border-radius: 4px; border-left: 4px solid #8FDB69;">Question {i+1}: ✓ Correct!</div>', unsafe_allow_html=True)
            elif selected:
                st.markdown(f'<div style="background-color: #FFEBEE; padding: 10px; border-radius: 4px; border-left: 4px solid #F44336;">Question {i+1}: ✗ Incorrect. The correct answer is: {correct}</div>', unsafe_allow_html=True)
    
    if download_button:
        quiz_json = json.dumps(quiz_data, indent=2)
        st.download_button(
            label="📥 Download as JSON",
            data=quiz_json,
            file_name="quiz.json",
            mime="application/json"
        )

def render_chat_page():
    main_header("🐙 Otto - Your TaskTamer Assistant")
    
    st.write("Hi, I'm Otto the Octopus! I can help you with task management, summarization, and quiz generation. Ask me anything about using TaskTamer or how to be more productive!")
    
   
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []
        
    for message in st.session_state.chat_history:
        role = message["role"]
        content = message["content"]
        
        if role == "user":
            st.markdown(f'<div class="user-message"><strong>You:</strong> {content}</div>', unsafe_allow_html=True)
        else:
            st.markdown(f'<div class="assistant-message"><strong>Otto:</strong> {content}</div>', unsafe_allow_html=True)
    
    # Ask a question
    question = st.text_input("Ask Otto a question:")
    
    if st.button("🐙 Send"):
        if not question:
            warning_box("Please enter a question")
            return
            
        # Add user message to chat history
        st.session_state.chat_history.append({"role": "user", "content": question})
        
        # Get the answer
        with st.spinner("Otto is thinking with all eight tentacles..."):
            answer = ask_question(question)
           
            if not answer.startswith("🐙"):
                answer = f"🐙 {answer}"
            
        # Add assistant message to chat history
        st.session_state.chat_history.append({"role": "assistant", "content": answer})
        
        # Rerun the app to show the updated chat
        st.rerun()
        
    # Clear chat button
    if st.session_state.chat_history:
        if st.button("🧹 Clear Chat"):
            st.session_state.chat_history = []
            st.rerun()
    
    # Example questions for empty chat
    if not st.session_state.chat_history:
        st.markdown("### Try asking me:")
        
        col1, col2 = st.columns(2)
        
        with col1:
            if st.button("How do I use the Task Breakdown feature?"):
                st.session_state.chat_history.append({"role": "user", "content": "How do I use the Task Breakdown feature?"})
                answer = ask_question("How do I use the Task Breakdown feature?")
                if not answer.startswith("🐙"):
                    answer = f"🐙 {answer}"
                st.session_state.chat_history.append({"role": "assistant", "content": answer})
                st.rerun()
                
            if st.button("Tips for staying focused"):
                st.session_state.chat_history.append({"role": "user", "content": "Can you give me tips for staying focused?"})
                answer = ask_question("Can you give me tips for staying focused?")
                if not answer.startswith("🐙"):
                    answer = f"🐙 {answer}"
                st.session_state.chat_history.append({"role": "assistant", "content": answer})
                st.rerun()
        
        with col2:
            if st.button("How can TaskTamer help with ADHD?"):
                st.session_state.chat_history.append({"role": "user", "content": "How can TaskTamer help with ADHD?"})
                answer = ask_question("How can TaskTamer help with ADHD?")
                if not answer.startswith("🐙"):
                    answer = f"🐙 {answer}"
                st.session_state.chat_history.append({"role": "assistant", "content": answer})
                st.rerun()
                
            if st.button("What's the best way to use the Quiz feature?"):
                st.session_state.chat_history.append({"role": "user", "content": "What's the best way to use the Quiz feature?"})
                answer = ask_question("What's the best way to use the Quiz feature?")
                if not answer.startswith("🐙"):
                    answer = f"🐙 {answer}"
                st.session_state.chat_history.append({"role": "assistant", "content": answer})
                st.rerun()
    
    info_box("""
    <b>🐙 Otto can help with:</b><br>
    • 🧩 Questions about TaskTamer features<br>
    • 🚀 Productivity techniques and advice<br>
    • 🧠 Focus and time management strategies<br>
    • ⚡ Tips for managing ADHD symptoms<br>
    • 🛑 Overcoming procrastination and distraction
    """)


def initialize_session_state():
    if "navigation" not in st.session_state:
        st.session_state.navigation = "Home"
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []
    if "quiz_answers" not in st.session_state:
        st.session_state.quiz_answers = {}
    if "quiz_submitted" not in st.session_state:
        st.session_state.quiz_submitted = False
    if "quiz_score" not in st.session_state:
        st.session_state.quiz_score = 0

# Function to navigate to a page
def navigate_to(destination):
    st.session_state.navigation = destination

def main():
    apply_styles()
    initialize_session_state()
    
    # Sidebar with logo
    st.sidebar.title("TaskTamer")
  
    
    # Navigation options
    options = {
        "Home": "🏠 Home",
        "Task Breakdown": "🧩 Task Breakdown",
        "Summarization": "📝 Summarization",
        "Quiz Generator": "🧠 Quiz Generator",
        "Chat": "🐙 Chat with Otto",
        "About": "ℹ️ About"
    }
    
    # Get current navigation state
    current_nav = st.session_state.navigation
    
    # Create sidebar navigation
    selection = st.sidebar.radio(
        "Navigation",
        list(options.keys()),
        format_func=lambda x: options[x],
        index=list(options.keys()).index(current_nav) if current_nav in options else 0,
        key="sidebar_navigation"
    )
    
    # Update navigation if selection changed
    if selection != current_nav:
        st.session_state.navigation = selection
        st.rerun()
    
    st.sidebar.markdown("---")
    
    # Sidebar info
    st.sidebar.info("**TaskTamer** helps you break down complex tasks, summarize content, and test your knowledge.\n\n🐙 Powered by Otto, your eight-tentacled productivity assistant!")
    
    # Otto's productivity tips
    with st.sidebar.expander("🐙 Otto's Productivity Tips"):
        tips = [
            "Break tasks into smaller steps to reduce overwhelm.",
            "Use the Pomodoro technique: 25 min focus, 5 min break.",
            "Try body-doubling: work alongside someone for accountability.",
            "Create a dedicated workspace to signal 'focus time' to your brain.",
            "Use visual timers to make time more concrete.",
            "Tackle your most challenging task when your energy is highest.",
            "Take strategic breaks to maintain mental energy."
        ]
        st.write(random.choice(tips))
    
    # Page rendering
    pages = {
        "Home": render_home_page,
        "Task Breakdown": render_task_page,
        "Summarization": render_summary_page,
        "Quiz Generator": render_quiz_page,
        "Chat": render_chat_page,
        "About": about_page.render_about_page
    }
    
    current_page = pages.get(selection)
    if current_page:
        current_page()
    else:
        # Fallback to home page
        render_home_page()

if __name__ == "__main__":
    main()