import streamlit as st
from backend.summarization import summarize_content, generate_study_notes
from ui.styles import main_header, section_header, warning_box, success_box, info_box
from utils.helpers import is_valid_url

def render_summary_page():
    main_header("Content Summarizer")
    
    st.write("Summarize text or web pages to extract key insights quickly.")
    
    with st.expander("Customize your summary"):
        col1, col2 = st.columns(2)
        
        with col1:
            format_type = st.radio(
                "Summary format",
                ["concise", "bullet", "detailed"],
                index=0,
                help="Choose how detailed your summary should be"
            )
        
        with col2:
            focus_area = st.radio(
                "Focus on",
                ["full document", "introduction", "body", "conclusion"],
                index=0,
                help="Choose which part of the document to focus on"
            )
            
            if focus_area == "full document":
                focus_area = None
    
    tab1, tab2, tab3 = st.tabs(["Text Input", "URL", "Study Notes"])
    
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
                summary = summarize_content(content=text_content, format_type=format_type, focus_area=focus_area)
                
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
                summary = summarize_content(url=url, format_type=format_type, focus_area=focus_area)
                
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
    
    with tab3:
        st.write("Generate comprehensive study notes from your content")
        
        col1, col2 = st.columns(2)
        
        with col1:
            study_text = st.text_area(
                "Enter study material:", 
                height=200,
                help="Paste the text you want to create study notes from"
            )
        
        with col2:
            st.write("Or enter a URL:")
            study_url = st.text_input(
                "Enter a webpage URL for study notes:",
                help="Works with most websites"
            )
        
        if st.button("Generate Study Notes"):
            content = None
            
            if study_text:
                content = study_text
            elif study_url and is_valid_url(study_url):
                with st.spinner("Fetching web content..."):
                    from backend.summarization import fetch_webpage_content
                    content = fetch_webpage_content(study_url)
            else:
                warning_box("Please enter either text or a valid URL")
                return
                
            if content and not content.startswith("Error"):
                with st.spinner("Generating study notes..."):
                    notes = generate_study_notes(content)
                
                section_header("Study Notes")
                st.markdown(notes)
                
                st.download_button(
                    label="Download Study Notes",
                    data=notes,
                    file_name="study_notes.md",
                    mime="text/markdown"
                )
                
                info_box("""
                <b>Study Tips:</b><br>
                • Review these notes within 24 hours to improve retention<br>
                • Create flashcards from the key concepts<br>
                • Explain the important points in your own words<br>
                • Connect new information to things you already know
                """)
            else:
                warning_box(f"Could not generate study notes: {content}")