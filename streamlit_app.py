import os
import streamlit as st
from dotenv import load_dotenv
from study_planner import StudyPlanner

# Load environment variables from .env file
load_dotenv()

def main():
    st.set_page_config(page_title="Study Plan Organizer", layout="wide")
    
    # Add the logo
    logo_path = "logo.png"
    st.image(logo_path, width=100)
    
    # Custom CSS for labels
    st.markdown(
        """
        <style>
        .custom-label {
            font-size: 1rem; 
            font-weight: Semi Bold;
        }
        .hidden-label {
            display: none;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    
    # Centered title and description
    st.markdown(
        """
        <div style="text-align: center;">
            <h1>Study Plan Organizer</h1>
            <p class="custom-label">This app helps you create a personalized study plan based on your available time slots and study materials.</p>
            <p>Simply enter your available study time slots and upload your study material in Markdown format. The app will generate a detailed study plan for you.</p>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    # Custom HTML for the labels
    st.markdown('<p class="custom-label">Enter your available study time slots:</p>', unsafe_allow_html=True)
    available_time_slots = st.text_input("Enter your available study time slots (e.g., 'Monday 10-12 and Tuesday 14-16' during 3 weeks):", label_visibility="collapsed")
    
    st.markdown('<p class="custom-label">Upload your study material (Markdown file):</p>', unsafe_allow_html=True)
    uploaded_file = st.file_uploader("Upload study material", type=["md"], label_visibility="collapsed")
    
    translate = st.checkbox("Show the study plan in Spanish")
    
    if uploaded_file is not None:
        text_path = f"/tmp/{uploaded_file.name}"
        with open(text_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        submit_button = st.button("Generate Study Plan")
        
        if submit_button:
            with st.spinner('Generating your study plan...'):
                planner = StudyPlanner()
                study_plan_summary = planner.generate_study_plan(available_time_slots, text_path, translate=translate)
                if study_plan_summary:
                    st.success("Study plan generated successfully!")
                    st.markdown("### Study Plan Summary:")
                    st.markdown(study_plan_summary)
                else:
                    st.error("Failed to generate study plan. Please check your inputs and try again.")
    else:
        st.info("Please upload your study material in Markdown format.")

if __name__ == "__main__":
    main()
