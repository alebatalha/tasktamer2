import streamlit as st

def apply_styles():
    
    st.markdown("""
    <style>
        /* Main color scheme from blue to purple gradient */
        :root {
            --blue-color: #1E88E5;
            --teal-color: #27C0AC;
            --green-color: #8FDB69;
            --purple-color: #9B4DCA;
            --light-purple-color: #D24CFF;
        }
        
        .main-header {
            font-size: 2.5rem;
            margin-bottom: 1.5rem;
            background: linear-gradient(90deg, var(--blue-color), var(--purple-color));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            font-weight: 700;
        }
        
        .section-header {
            font-size: 1.8rem;
            margin-top: 2rem;
            margin-bottom: 1rem;
            background: linear-gradient(90deg, var(--blue-color), var(--teal-color));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            font-weight: 600;
        }
        
        .info-box {
            background-color: #E3F2FD;
            border-left: 5px solid var(--blue-color);
            border-radius: 0.5rem;
            padding: 1.2rem;
            margin-bottom: 1.5rem;
        }
        
        .success-box {
            background-color: #E8F5E9;
            border-left: 5px solid var(--green-color);
            border-radius: 0.5rem;
            padding: 1.2rem;
            margin-bottom: 1.5rem;
        }
        
        .warning-box {
            background-color: #FFF8E1;
            border-left: 5px solid var(--teal-color);
            border-radius: 0.5rem;
            padding: 1.2rem;
            margin-bottom: 1.5rem;
        }
        
        .task-item {
            background-color: #FAFAFA;
            border-left: 4px solid var(--blue-color);
            padding: 1rem;
            margin-bottom: 0.8rem;
            border-radius: 0 0.5rem 0.5rem 0;
            font-size: 1.05rem;
        }
        
        /* Enhanced Task Breakdown Styles */
        .task-overview {
            background-color: #F3F6FF;
            border-radius: 0.8rem;
            padding: 1.5rem;
            margin-bottom: 1.5rem;
            border: 1px solid #E1E5F2;
        }
        
        .step-card {
            background: white;
            border-radius: 8px;
            padding: 16px;
            margin-bottom: 16px;
            box-shadow: 0 2px 5px rgba(0,0,0,0.05);
            border-left: 4px solid var(--blue-color);
        }
        
        .step-heading {
            font-weight: 600;
            font-size: 1.1rem;
            margin-bottom: 8px;
            color: #2C3E50;
        }
        
        .step-meta {
            display: flex;
            font-size: 0.9rem;
            color: #7F8C8D;
            margin-bottom: 12px;
        }
        
        .step-meta-item {
            margin-right: 16px;
        }
        
        .step-tip {
            background: #F8F9FA;
            padding: 10px;
            border-radius: 6px;
            font-size: 0.9rem;
            border-left: 3px solid var(--teal-color);
        }
        
        .step-high {
            border-left: 4px solid #FF5252;
        }
        
        .step-medium {
            border-left: 4px solid #FFC107;
        }
        
        .step-low {
            border-left: 4px solid #4CAF50;
        }
        
        .reward-card {
            background: linear-gradient(135deg, #E3F2FD, #F3E5F5);
            border-radius: 8px;
            padding: 16px;
            margin-top: 24px;
            border: 1px dashed var(--purple-color);
        }
        
        /* Stylize buttons */
        .stButton>button {
            background: linear-gradient(90deg, var(--blue-color), var(--purple-color));
            color: white;
            font-weight: 500;
            border: none;
            border-radius: 0.3rem;
            padding: 0.5rem 1rem;
            transition: all 0.3s ease;
        }
        
        .stButton>button:hover {
            background: linear-gradient(90deg, var(--purple-color), var(--blue-color));
            transform: translateY(-2px);
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        }
        
        /* Tabs styling */
        .stTabs [data-baseweb="tab-list"] {
            gap: 2px;
        }
        
        .stTabs [data-baseweb="tab"] {
            background-color: #F3F4F6;
            padding: 10px 20px;
            border-radius: 4px 4px 0 0;
        }
        
        .stTabs [aria-selected="true"] {
            background: linear-gradient(90deg, var(--blue-color), var(--teal-color));
            color: white;
        }
                /* Chat message styling */
        .user-message {
            background-color: #F0F4FF;
            padding: 12px;
            border-radius: 10px 10px 0 10px;
            margin: 10px 0;
            align-self: flex-end;
            max-width: 80%;
        }
        
        .assistant-message {
            background: linear-gradient(135deg, #E2F0FF, #F2E7FF);
            padding: 12px;
            border-radius: 10px 10px 10px 0;
            margin: 10px 0;
            align-self: flex-start;
            max-width: 80%;
        }
        
        /* Logo styling */
        .logo-text {
            font-size: 2rem;
            font-weight: 800;
            letter-spacing: 1px;
            background: linear-gradient(90deg, var(--blue-color), var(--light-purple-color));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }
        
        .getting-things-done {
            font-size: 0.9rem;
            color: var(--green-color);
            font-weight: 500;
            margin-left: 10px;
        }
        
        /* Quiz styling */
        .quiz-question {
            background-color: #F8F9FA;
            padding: 15px;
            border-radius: 8px;
            margin-bottom: 20px;
            border-left: 4px solid var(--blue-color);
        }
        
        .correct-answer {
            background-color: #E8F5E9;
            padding: 10px;
            border-radius: 4px;
            border-left: 4px solid var(--green-color);
        }
        
        .incorrect-answer {
            background-color: #FFEBEE;
            padding: 10px;
            border-radius: 4px;
            border-left: 4px solid #F44336;
        }
        
        /* Custom footer */
        .footer {
            margin-top: 3rem;
            padding-top: 1rem;
            border-top: 1px solid #E0E0E0;
            text-align: center;
            color: #757575;
            font-size: 0.9rem;
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


def task_item(text, idx=None, completed=False):
    
    prefix = f"{idx}. " if idx is not None else ""
    task_class = "task-item" + (" task-completed" if completed else "")
    st.markdown(f'<div class="{task_class}">{prefix}{text}</div>', unsafe_allow_html=True)


def render_step_card(step):
    
    priority_class = f"step-{step['priority'].lower()}" if 'priority' in step else ""
    
    st.markdown(f'<div class="step-card {priority_class}">', unsafe_allow_html=True)
    st.markdown(f'<div class="step-heading">Step {step["number"]}: {step["description"]}</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="step-meta">', unsafe_allow_html=True)
    if 'time' in step:
        st.markdown(f'<div class="step-meta-item">⏱️ Time: {step["time"]} min</div>', unsafe_allow_html=True)
    if 'priority' in step:
        st.markdown(f'<div class="step-meta-item">🔍 Priority: {step["priority"]}</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    if 'adhd_tip' in step:
        st.markdown(f'<div class="step-tip">💡 ADHD Tip: {step["adhd_tip"]}</div>', unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)


def render_footer():

    import datetime
    current_year = datetime.datetime.now().year
    st.markdown(f'<div class="footer">© {current_year} TaskTamer by Alessandra Batalha. All rights reserved.</div>', unsafe_allow_html=True)


def logo_header():

    st.markdown(
        '<div style="display: flex; align-items: center;">'
        '<span class="logo-text">TASK TAMER</span>'
        '<span class="getting-things-done">GETTING THINGS DONE</span>'
        '</div>', 
        unsafe_allow_html=True
    )