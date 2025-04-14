import streamlit as st
from ui.styles import main_header, section_header, info_box, render_footer

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
    - **NLTK** for natural language processing and text analysis
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
    
    
    st.markdown("---")
    st.caption("TaskTamer version 2.0")
    import datetime
    current_year = datetime.datetime.now().year
    st.caption(f"© {current_year} Alessandra Batalha. All rights reserved.")
