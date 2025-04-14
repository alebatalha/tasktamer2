import streamlit as st
import json
from backend.task_breakdown import TaskBreakdown
from ui.styles import main_header, section_header, warning_box, render_step_card

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