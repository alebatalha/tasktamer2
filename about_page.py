import streamlit as st

def main_header(text):
    st.markdown(f'<h1 style="font-size: 2.5rem; margin-bottom: 1rem;">{text}</h1>', unsafe_allow_html=True)

def section_header(text):
    st.markdown(f'<h2 style="font-size: 1.8rem; margin-top: 1.5rem; margin-bottom: 1rem;">{text}</h2>', unsafe_allow_html=True)

def info_box(text):
    st.markdown(f'<div style="background-color: #f0f2f6; border-radius: 0.5rem; padding: 1rem; margin-bottom: 1rem;">{text}</div>', unsafe_allow_html=True)

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
        st.markdown("#### Task Breakdown")
        st.write("Convert complex tasks into manageable, actionable steps")
        
        st.markdown("#### Content Summarization")
        st.write("Extract key insights from text, web pages, and YouTube videos")
    
    with col2:
        st.markdown("#### Quiz Generation")
        st.write("Create interactive quizzes from any content to test your knowledge")
        
        st.markdown("#### AI Assistant")
        st.write("Ask questions about the content and get intelligent responses")
    
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
    For more information about this project or to provide feedback, please contact Alessandra Batalha via Dublin Business School.
    """)

if __name__ == "__main__":
    render_about_page()