from crewai import Agent
from crewai_tools import FileReadTool




#@agentops.track_agent(name="Study Planner")
class Agents:
    def study_planner_agent(self):
        return Agent(
            role="Study Planner",
            goal="Organize your study schedule based on your available time.",
            verbose=True,
            #tools=[SerperDevTool(n_results=5), ScrapeWebsiteTool()],
            tools=[FileReadTool(file_path='./output/md_analysis_summary.md'), FileReadTool(file_path='./output/time_estimation.md')],
            backstory=(
                "You are an expert that give courses of how to study better." 
                "With a focus on efficiency and organization, "
                "you specialize in creating personalized study schedules "
                "to help users effectively manage their time and achieve their learning goals."
                "You need to consider the extracted content from the file to create a tailored study plan."
                "Try to optimize their learning experience and make the most of their available time."
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
                "Pay attention to the number of pages and the complexity of the content to provide accurate estimates."
                "Check the available time slots to suggest the user the best way to study the content,"
                "and if the content is too much for the available time, suggest the user to split the content in different days."
                "Pay attention to the titles and subtitles of the content to estimate the time needed to study each topic."
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
                "If the content is too much, we need to suggest the user that the time is not enough to study all the content."
            ),
            verbose=True,
            tools=[FileReadTool(file_path='./output/personalized_study_plan.md')],
            backstory=(
                "With a focus on quality assurance and attention to detail, "
                "you excel at ensuring that the final output meets the highest standards "
                "and that all components of the study plan are well-structured and accurate."
            )
        )

    def translation_agent(self):
        return Agent(
            role='Translation Expert',
            goal=(
                "Translate the content of the study plan into Spanish,"
                "or vice versa, to help users access information in their preferred language."
            ),
            verbose=True,
            tools=[FileReadTool(file_path='./output/final_study_plan.md')],
            backstory=(
                "With a focus on language translation, "
                "you specialize in translating content from one language to another "
                "to help users access information in their preferred language."
                "You need to keep the same format and structure of the study plan but in Spanish."
                "For example if is a markdown file, you need to keep the same format but in Spanish."
            )
        )