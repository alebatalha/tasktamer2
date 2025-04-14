import streamlit as st
import json
from backend.question_generation import generate_quiz
from ui.styles import main_header, section_header, warning_box, success_box, info_box
from utils.helpers import is_valid_url

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

def display_quiz(quiz_data):
    if not quiz_data:
        warning_box("Could not generate quiz. Please try with different content.")
        return
    
   
    if isinstance(quiz_data, list) and quiz_data and "error" in quiz_data[0]:
        warning_box(quiz_data[0]["error"])
        return
        
    section_header("Your Quiz")
    
    if "quiz_answers" not in st.session_state:
        st.session_state.quiz_answers = {}
        st.session_state.quiz_submitted = False
        st.session_state.quiz_score = 0
    
    for i, question in enumerate(quiz_data):
        st.markdown(f'<div class="quiz-question">', unsafe_allow_html=True)
        st.subheader(f"Question {i+1}")
        question_text = question.get("question", "No question available.")
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
        submit_button = st.button("Submit Quiz")
    
    with col2:
        download_button = st.button("Download Quiz")
    
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
        success_box(f"Your score: {st.session_state.quiz_score}/{len(quiz_data)} ({score_percentage:.1f}%)")
        
        for i in range(len(quiz_data)):
            answer_key = f"q_{i}"
            selected = st.session_state.get(f"quiz_{i}", "")
            correct = st.session_state.quiz_answers.get(answer_key, "")
            
            if selected and selected == correct:
                st.markdown(f'<div class="correct-answer">Question {i+1}: ✓ Correct!</div>', unsafe_allow_html=True)
            elif selected:
                st.markdown(f'<div class="incorrect-answer">Question {i+1}: ✗ Incorrect. The correct answer is: {correct}</div>', unsafe_allow_html=True)
    
    if download_button:
        quiz_json = json.dumps(quiz_data, indent=2)
        st.download_button(
            label="Download as JSON",
            data=quiz_json,
            file_name="quiz.json",
            mime="application/json"
        )
    
    if "quiz_history" in st.session_state and st.session_state.quiz_history:
        with st.expander("Quiz History"):
            history_data = {
                "Date": [],
                "Questions": [],
                "Score": [],
                "Percentage": []
            }
            
            for item in st.session_state.quiz_history:
                history_data["Date"].append(item["timestamp"])
                history_data["Questions"].append(item["questions"])
                history_data["Score"].append(item["score"])
                history_data["Percentage"].append(f"{item['percentage']:.1f}%")
            
            st.dataframe(history_data)
            
            if len(st.session_state.quiz_history) >= 2:
                st.subheader("Performance Over Time")
                chart_data = {
                    "Quiz": list(range(1, len(st.session_state.quiz_history) + 1)),
                    "Score (%)": [item["percentage"] for item in st.session_state.quiz_history]
                }
                st.line_chart(chart_data)
                
                avg_score = sum(item["percentage"] for item in st.session_state.quiz_history) / len(st.session_state.quiz_history)
                trend = "improving" if st.session_state.quiz_history[-1]["percentage"] > avg_score else "consistent"
                
                info_box(f"""
                <b>Performance Insight:</b><br>
                Your average quiz score is {avg_score:.1f}%. Your performance appears to be {trend}.
                Regular quizzing helps strengthen memory retention through active recall!
                """)