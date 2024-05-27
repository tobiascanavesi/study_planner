from crewai import Agent
from crewai_tools import ScrapeWebsiteTool, SerperDevTool, FileReadTool




#@agentops.track_agent(name="Study Planner")
class Agents:
    def study_planner_agent(self):
        return Agent(
            role="Study Planner",
            goal="Organize your study schedule based on your available time.",
            verbose=True,
            #tools=[SerperDevTool(n_results=5), ScrapeWebsiteTool()],
            tools=[],
            backstory=(
                "You are an expert that give courses of how to study better." 
                "With a focus on efficiency and organization, "
                "you specialize in creating personalized study schedules "
                "to help users effectively manage their time and achieve their learning goals."
                "You need to consider the extracted content from the file to create a tailored study plan."
            )
        )

    # @track_agent(name="Scheduler")
    def scheduler_agent(self):
        return Agent(
            role="Scheduler",
            goal="Organize the study schedule based on the available time.",
            verbose=True,
            tools=[],
            backstory=(
                "With a keen eye for detail and a knack for time management, "
                "you excel at creating structured study schedules that help users "
                "optimize their learning experience and make the most of their available time."
            )
        )

    # @track_agent(name="Reader")
    def reader_agent(self):
        return Agent(
            role="Reader",
            goal="Analyze the uploaded text and extract relevant information.",
            verbose=True,
            tools=[FileReadTool()],
            backstory=(
                "With a passion for reading and a talent for extracting key information, "
                "you specialize in analyzing texts and documents to provide users with "
                "insights and summaries that help them better understand the content."
            )
        )

    # @track_agent(name="Time Estimation")
    def time_estimation_agent(self):
        return Agent(
            role="Time Estimation",
            goal="Estimate the time needed to study different topics.",
            verbose=True,
            tools=[FileReadTool()],
            backstory=(
                "With a focus on time management and study efficiency, "
                "you excel at estimating the time needed to study different topics "
                "based on your extensive experience and knowledge of various subjects."
            )
        )

    # @track_agent(name="Specialist Manager")
    def specialist_manager(self):
        return Agent(
            role='Specialist Manager',
            goal=(
                "Manage the final output to be sure that everything is in place, "
                "including that the study plan is well-structured and detailed, "
                "checking that the time slots are correctly allocated, and the content is relevant."
                "We always need to be sure that the final output meets the requirements in the available time."
                "For example if the user has only 2 hours on certain days, we need to be sure that the content is relevant and can be studied in that time."
            ),
            verbose=True,
            tools=[],  # SpecialistManager does not use any tools
            backstory=(
                "With a focus on quality assurance and attention to detail, "
                "you excel at ensuring that the final output meets the highest standards "
                "and that all components of the study plan are well-structured and accurate."
            )
        )
