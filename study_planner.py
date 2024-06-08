from crewai import Crew, Process
from langchain_openai import ChatOpenAI
from tasks import Tasks
from agents import Agents
import os

#import agentops

class StudyPlanner:
    def __init__(self):
        #agentops.init(tags=['study_planner'],max_wait_time=3)
        self.tasks = Tasks()
        self.agents = Agents()
        self.study_plan_crew = Crew(
            agents=[
                self.agents.reader_agent(), 
                self.agents.time_estimation_agent(), 
                self.agents.study_planner_agent(), 
                self.agents.specialist_manager(),
                self.agents.translation_agent()
            ],
            tasks=[
                self.tasks.analyze_text_content_task(), 
                self.tasks.time_estimation_task(), 
                self.tasks.study_plan_task(), 
                self.tasks.manage_final_output_task(),
                self.tasks.translation_task()
            ],
            # You can add here a custom model for the manager but this is optional.
            # manager_llm=ChatOpenAI(model="gpt-4-turbo", temperature=0.6),
            # process=Process.hierarchical,
            verbose=2,
            memory=True
        )

    def generate_study_plan(self, available_time_slots, text_path, translate=False):
        # Kickoff the Crew AI process
        result = self.study_plan_crew.kickoff(inputs={"available_time_slots": available_time_slots, "text_path": text_path})

        # Return study plan summary
        if result:
            script_dir = os.path.dirname(os.path.abspath(__file__))
            if translate:
                file_path = os.path.join(script_dir, "output", "spanish_study_plan.md")
            else :
                file_path = os.path.join(script_dir, "output", "final_study_plan.md")
            
            with open(file_path, "r") as f:
                study_plan_summary = f.read()
            return study_plan_summary
        else:
            return None
