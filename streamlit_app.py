import streamlit as st
import re
import json
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

def initialize_session_state():
    """Initialize all session state variables needed by the application."""
    if "initialized" not in st.session_state:
        st.session_state.initialized = True
        st.session_state.task_data = {}
        st.session_state.quiz_history = []
        st.session_state.chat_history = {}
        st.session_state.quiz_answers = {}
        st.session_state.quiz_submitted = False
        st.session_state.quiz_score = 0
        st.session_state.navigation = "Home"

def main():
    try:
       
        apply_styles()
        
     
        initialize_session_state()
        
       
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