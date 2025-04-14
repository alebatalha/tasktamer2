import streamlit as st
from backend.chat_assistant import ask_question
from ui.styles import main_header, info_box, warning_box

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
            try:
                answer = ask_question(question)
            except Exception as e:
                answer = f"I'm sorry, I encountered an error: {str(e)}. Could you try asking your question differently?"
            
   
        st.session_state.chat_history.append({"role": "assistant", "content": answer})
        
        st.rerun()  
    if st.session_state.chat_history:
        if st.button("Clear Chat"):
            st.session_state.chat_history = []
            st.rerun()  

    if not st.session_state.chat_history:
        st.markdown("### Try asking me:")
        
        col1, col2 = st.columns(2)
        
        with col1:
            if st.button("How do I use the Task Breakdown feature?"):
                st.session_state.chat_history.append({"role": "user", "content": "How do I use the Task Breakdown feature?"})
                answer = ask_question("How do I use the Task Breakdown feature?")
                st.session_state.chat_history.append({"role": "assistant", "content": answer})
                st.rerun() 
            if st.button("Tips for staying focused"):
                st.session_state.chat_history.append({"role": "user", "content": "Can you give me tips for staying focused?"})
                answer = ask_question("Can you give me tips for staying focused?")
                st.session_state.chat_history.append({"role": "assistant", "content": answer})
                st.rerun()  
        with col2:
            if st.button("How can TaskTamer help with ADHD?"):
                st.session_state.chat_history.append({"role": "user", "content": "How can TaskTamer help with ADHD?"})
                answer = ask_question("How can TaskTamer help with ADHD?")
                st.session_state.chat_history.append({"role": "assistant", "content": answer})
                st.rerun() 
            if st.button("What's the best way to use the Quiz feature?"):
                st.session_state.chat_history.append({"role": "user", "content": "What's the best way to use the Quiz feature?"})
                answer = ask_question("What's the best way to use the Quiz feature?")
                st.session_state.chat_history.append({"role": "assistant", "content": answer})
                st.rerun()  
    
    info_box("""
    <b>Otto can help with:</b><br>
    • Questions about TaskTamer features<br>
    • Productivity techniques and advice<br>
    • Focus and time management strategies<br>
    • Tips for managing ADHD symptoms<br>
    • Overcoming procrastination and distraction
    """)