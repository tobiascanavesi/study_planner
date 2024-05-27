import os
from dotenv import load_dotenv
import streamlit as st
from study_planner import StudyPlanner

load_dotenv()

def main():
    st.title("Study Plan Organizer")

    # Brief introduction
    st.write("""
    Welcome to the Study Plan Organizer! This app helps you create a personalized study plan based on your available time slots and study materials.
    Simply enter your available study time slots and upload your study material in Markdown format. The app will generate a detailed study plan for you.
    """)

    # User input for available time slots
    available_time_slots = st.text_input("Enter your available study time slots (e.g., 'Monday 10-12 and Tuesday 14-16' during 3 weeks.):")

    # File uploader for Markdown file
    uploaded_file = st.file_uploader("Upload your study material (Markdown file)", type="md")

    if uploaded_file is not None:
        text_path = f"/tmp/{uploaded_file.name}"
        with open(text_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        # Button to generate study plan
        submit_button = st.button("Generate Study Plan")

        if submit_button:
            # Show spinner while generating study plan
            with st.spinner('Generating your study plan...'):
                # Generate study plan
                planner = StudyPlanner()
                study_plan_summary = planner.generate_study_plan(available_time_slots, text_path)
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
