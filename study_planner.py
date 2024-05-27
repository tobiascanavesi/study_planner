import os
from crewai import Task, Crew, Process
from crewai_tools import FileReadTool, SerperDevTool, ScrapeWebsiteTool
from crewai_components import Agents

class StudyPlanner:
    def __init__(self):
        self.agents = Agents()

    def generate_study_plan(self, available_time_slots, text_path):
        try:
            # Initialize the tasks
            analyze_text_task = self.analyze_text_content_task(text_path)
            time_estimation_task = self.time_estimation_task(analyze_text_task, available_time_slots)
            study_plan_task = self.study_plan_task(analyze_text_task, time_estimation_task, available_time_slots)
            final_output_task = self.manage_final_output_task(study_plan_task, available_time_slots)

            # Create a crew with the tasks
            crew = Crew(
                agents=[self.agents.reader_agent(), self.agents.time_estimation_agent(), self.agents.scheduler_agent(), self.agents.specialist_manager()],
                tasks=[analyze_text_task, time_estimation_task, study_plan_task, final_output_task],
                process=Process.sequential
            )

            # Kick off the crew to execute tasks
            result = crew.kickoff(inputs={'text_path': text_path, 'available_time_slots': available_time_slots})
            return result
        except Exception as e:
            print(f"Error generating study plan: {e}")
            return None

    def analyze_text_content_task(self, text_path):
        return Task(
            description=("Analyze the text content {text_path} to extract key insights for study planning."
                         "This includes summarizing the content, identifying key topics, and estimating the number of pages."),
            expected_output=("A summary of key insights from the text content."
                             "The number of pages in that text and the main topics covered."),
            tools=[FileReadTool()],
            agent=self.agents.reader_agent(),
            async_execution=False,
            output_file="md_analysis_summary.md"
        )

    def time_estimation_task(self, analyze_text_task, available_time_slots):
        return Task(
            description=("Estimate the time needed to study different topics based on the extracted content."
                         "And the available time slots {available_time_slots}, and the number of pages in the text."),
            expected_output="An estimated study time for each topic and suggestions for optimizing study time.",
            context=[analyze_text_task],
            agent=self.agents.time_estimation_agent(),
            output_file="time_estimation.md"
        )

    def study_plan_task(self, analyze_text_task, time_estimation_task, available_time_slots):
        return Task(
            description="Create a personalized study schedule based on the extracted content and available time slots that are {available_time_slots}.",
            expected_output="A detailed study schedule, study tips, and estimated number of pages to study.",
            context=[analyze_text_task, time_estimation_task],
            agent=self.agents.scheduler_agent(),
            output_file="personalized_study_plan.md"
        )

    def manage_final_output_task(self, study_plan_task, available_time_slots):
        return Task(
            description=("Manage the final output to ensure quality and accuracy."
                         "We must make sure that the content to be studied is distributed in the time that the user has enabled the {available_time_slots}."),
            expected_output="A well-structured and detailed study plan that meets the highest standards.",
            context=[study_plan_task],
            tools=[SerperDevTool(n_results=3), ScrapeWebsiteTool()],
            agent=self.agents.specialist_manager(),
            output_file="final_study_plan.md"
        )
