import streamlit as st

def main_header(text):
    st.markdown(f'<h1 style="font-size: 2.5rem; background: linear-gradient(90deg, #00BCD4, #9C27B0); -webkit-background-clip: text; -webkit-text-fill-color: transparent; font-weight: 700; margin-bottom: 1rem;">{text}</h1>', unsafe_allow_html=True)

def section_header(text):
    st.markdown(f'<h2 style="font-size: 1.8rem; background: linear-gradient(90deg, #1E88E5, #00BCD4); -webkit-background-clip: text; -webkit-text-fill-color: transparent; font-weight: 600; margin-top: 1.5rem; margin-bottom: 1rem;">{text}</h2>', unsafe_allow_html=True)

def info_box(text):
    st.markdown(f'<div style="background-color: rgba(0, 188, 212, 0.1); border-left: 5px solid #00BCD4; border-radius: 0.5rem; padding: 1.2rem; margin-bottom: 1.5rem; box-shadow: 0 2px 5px rgba(0,0,0,0.05);">{text}</div>', unsafe_allow_html=True)

def render_about_page():
    main_header("About TaskTamer")
    
    st.write("""
    TaskTamer is a productivity tool designed to help users manage their learning and workflow more effectively. 
    The application combines several powerful features to break down complex tasks, summarize content, and generate 
    quizzes for better knowledge retention - all with the help of Otto, your eight-tentacled productivity assistant!
    """)
    
    section_header("Key Features")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### 🧩 Task Breakdown")
        st.write("Convert complex tasks into manageable, actionable steps")
        
        st.markdown("#### 📝 Content Summarization")
        st.write("Extract key insights from text, web pages, and YouTube videos")
    
    with col2:
        st.markdown("#### 🧠 Quiz Generation")
        st.write("Create interactive quizzes from any content to test your knowledge")
        
        st.markdown("#### 🐙 Otto - Your Assistant")
        st.write("Ask questions and get help anytime")
    
    section_header("Why TaskTamer Was Created")
    
    st.write("""
    TaskTamer was created specifically to assist learners, primarily those with ADHD, through educational 
    and task management features. The tool addresses common challenges faced by students with attention difficulties:
    """)
    
    st.markdown("""
    - **Information Overload**: Summarizing helps condense large amounts of information into digestible chunks
    - **Task Organization**: Breaking down complex tasks makes them less overwhelming
    - **Knowledge Retention**: Quiz generation reinforces learning through active recall
    - **Accessibility**: Simple interface designed for all cognitive styles
    """)
    
    st.write("""
    The vision was to develop a virtual assistant that adapts to students' requirements by offering 
    personalized recommendations and improved accessibility, making learning more inclusive.
    """)
    
    section_header("Meet Otto - Your Eight-Tentacled Assistant")
    
    st.write("""
    Otto is your friendly octopus productivity assistant! Just like real octopuses are known for their intelligence and 
    problem-solving abilities, Otto is designed to help you tackle complex challenges with creative solutions.
    
    With eight helpful tentacles, Otto can:
    
    - Break down complex tasks into manageable steps
    - Extract key information from lengthy content
    - Create engaging quizzes to test your knowledge
    - Provide personalized productivity advice
    - Offer ADHD-friendly strategies for maintaining focus and motivation
    - Share tips for overcoming procrastination and managing your time effectively
    """)
    
    section_header("About the Developer")
    
    st.write("""
    TaskTamer was created by **Alessandra Batalha** as part of her final year project at Dublin Business School. 
    The project represents the culmination of her studies in Computer Science, combining practical software 
    engineering skills with artificial intelligence techniques.
    """)
    
    st.write("""
    Alessandra developed TaskTamer with a focus on helping students and professionals manage their learning and 
    work tasks more efficiently. The project demonstrates her skills in full-stack development, natural language 
    processing, and user experience design.
    """)
    
    info_box("""
    <b>Contact:</b><br>
    For more information about this project or to provide feedback, please contact Alessandra Batalha<br><br>
    <b>GitHub:</b> <a href="https://github.com/alebatalha" target="_blank">@alebatalha</a>
    """)
    
   
    st.markdown("""
    <div style="margin-top: 30px; padding-top: 20px; border-top: 1px solid #e0e0e0; text-align: center; color: #757575; font-size: 0.9rem; animation: pulse 2s infinite;">
        <p>TaskTamer Version 2.0</p>
        <p>Made with 🐙 and ❤️</p>
    </div>
    <style>
    @keyframes pulse {
        0% { opacity: 0.8; }
        50% { opacity: 1; }
        100% { opacity: 0.8; }
    }
    </style>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    render_about_page()