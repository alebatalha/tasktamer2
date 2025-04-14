import streamlit as st
from ui.styles import main_header, info_box, logo_header

def render_home_page():
    
    logo_header()
    
    st.write("Your personal productivity assistant that helps you break down complex tasks, summarize information, and generate quizzes.")
    
  
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("🧩 Task Breakdown")
        st.write("Turn overwhelming tasks into manageable steps")
        if st.button("Try Task Breakdown", key="task_btn"):
            st.session_state["navigation"] = "Task Breakdown"
            st.experimental_rerun()
            
        st.subheader("📝 Summarization")
        st.write("Extract key insights from text and web pages")
        if st.button("Try Summarization", key="summary_btn"):
            st.session_state["navigation"] = "Summarization"
            st.experimental_rerun()
            
    with col2:
        st.subheader("🧠 Quiz Generator")
        st.write("Create quizzes from your learning materials")
        if st.button("Try Quiz Generator", key="quiz_btn"):
            st.session_state["navigation"] = "Quiz Generator"
            st.experimental_rerun()
            
        st.subheader("🤖 Otto - Your Assistant")
        st.write("Ask questions and get help anytime")
        if st.button("Ask Otto", key="otto_btn"):
            st.session_state["navigation"] = "Otto Assistant"
            st.experimental_rerun()
    
   
    info_box("""
    <b>Getting Started:</b>
    <ol>
        <li>Select a feature from the sidebar</li>
        <li>Enter your task or content</li>
        <li>Get instant results!</li>
    </ol>
    """)
    
 
    st.markdown("---")
    st.subheader("✨ How TaskTamer Helps You")
    
   
    with st.expander("Task Breakdown - Conquer large projects"):
        st.write("""
        Breaking down large, complex tasks into manageable steps helps reduce overwhelm and makes progress easier to track.
        TaskTamer analyzes your task description and creates a personalized, step-by-step plan that's easy to follow.
        
        Features:
        - Different detail levels to match your needs
        - ADHD-friendly tips included with each step
        - Time estimates and priority levels
        - Downloadable action plans
        """)
        
    with st.expander("Summarization - Extract key insights"):
        st.write("""
        Information overload is a common productivity killer. TaskTamer's summarization feature helps you quickly extract
        the most important points from any text or webpage, saving you time and improving comprehension.
        
        Features:
        - Summarize long articles, documents, or web pages
        - Different summary formats (concise, bullet points, or detailed)
        - Focus on specific sections like introductions or conclusions
        - Create comprehensive study notes
        """)
        
    with st.expander("Quiz Generator - Test your knowledge"):
        st.write("""
        Active recall is one of the most effective study techniques. TaskTamer turns your content into interactive quizzes
        that help you reinforce learning and identify knowledge gaps.
        
        Features:
        - Create quizzes from any text or webpage
        - Customizable number of questions
        - Track your performance over time
        - Downloadable quizzes for later use
        """)
        
    with st.expander("Otto Assistant - Get personalized help"):
        st.write("""
        Otto is your friendly productivity assistant, ready to answer questions and provide guidance on using TaskTamer
        or improving your productivity in general.
        
        Features:
        - Get help with using TaskTamer features
        - Ask about productivity techniques
        - Get personalized advice for focus and time management
        - Tips for managing ADHD and overcoming procrastination
        """)
    

    import random
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
    
    st.markdown("---")
    st.markdown("### 💡 Productivity Tip of the Day")
    st.markdown(f"*\"{random.choice(productivity_tips)}\"*")