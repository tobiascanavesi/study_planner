from crewai import Task
from crewai_tools import ScrapeWebsiteTool, SerperDevTool, FileReadTool
from agents import Agents

class Tasks:
    def __init__(self):
        self.agents = Agents()

    def analyze_text_content_task(self):
        return Task(
            description=("Analyze the text content {text_path} to extract key insights for study planning."
                         "This includes summarizing the content, identifying key topics, and estimating the number of pages."),
            expected_output=("A summary of key insights from the text content."
                             "The number of pages in that text and the main topics covered."
                             "Important data for the time estimation agent, that will estimate the time needed to study different topics."),
            tools=[],
            agent = self.agents.reader_agent(),
            async_execution = False,
            output_file="/output/md_analysis_summary.md"
        )

    def time_estimation_task(self):
        return Task(
            description=("Estimate the time needed to study different topics based on the extracted content."
                         "And the available time slots {available_time_slots}, and the number of pages in the text that could be a markdown or pdf."),
            expected_output = "An estimated study time for each topic and suggestions for optimizing study time.",
            context = [self.analyze_text_content_task()],
            agent = self.agents.time_estimation_agent(),
            output_file = "/output/time_estimation.md"
        )

    def study_plan_task(self):
        return Task(
            description="Create a personalized study schedule based on the extracted content and available time slots that are {available_time_slots}.",
            expected_output=("A detailed study schedule, study tips, and estimated number of pages to study."
                             "The study plan should be optimized for the user's available time example:"
                             "Monday, in the available time slot, study 'Topic A' for the available time."
                             "So on for the rest of the available time slots."),
            context=[self.analyze_text_content_task(), self.time_estimation_task()],
            agent = self.agents.study_planner_agent(),
            output_file = "/output/personalized_study_plan.md"
        )

    def manage_final_output_task(self):
        return Task(
            description=("Manage the final output to ensure quality and accuracy."
                         "We must make sure that the content to be studied is distributed in the time that the user has enabled the {available_time_slots}."
                         "Is important to check the study plan, the time slots, and the content to be studied match the user's requirements."),
            expected_output="A well-structured and detailed study plan that meets the highest standards.",
            context=[self.study_plan_task()],
            tools=[], # You can try to give to out manager this kind of tools [SerperDevTool(n_results=3), ScrapeWebsiteTool()],
            agent = self.agents.specialist_manager(),
            output_file = "/output/final_study_plan.md"
        )
        
    def translation_task(self):
        return Task(
            description=("Translate the study plan to Spanish."),
            expected_output="A translated version of the study plan in Spanish.",
            context=[self.manage_final_output_task()],
            tools=[],
            agent = self.agents.translation_agent(),
            output_file = "/output/spanish_study_plan.md"
        )
