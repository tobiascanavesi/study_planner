from crewai import Crew, Process
from langchain_openai import ChatOpenAI
from tasks import Tasks
from agents import Agents

#import agentops

class StudyPlanner:
    def __init__(self):
        #agentops.init(tags=['study_planner'],max_wait_time=3)
        self.tasks = Tasks()
        self.agents = Agents()
        self.study_plan_crew = Crew(
            agents=[
                self.agents.study_planner_agent(), 
                self.agents.reader_agent(), 
                self.agents.time_estimation_agent(), 
                self.agents.specialist_manager()
            ],
            tasks=[
                self.tasks.analyze_text_content_task(), 
                self.tasks.time_estimation_task(), 
                self.tasks.study_plan_task(), 
                self.tasks.manage_final_output_task()
            ],
            # You can add here a custom model for the manager but this is optional.
            # manager_llm=ChatOpenAI(model="gpt-4-turbo", temperature=0.6),
            # process=Process.hierarchical,
            verbose=2,
            memory=True
        )

    def generate_study_plan(self, available_time_slots, text_path):
        # Kickoff the Crew AI process
        result = self.study_plan_crew.kickoff(inputs={"available_time_slots": available_time_slots, "text_path": text_path})

        # Return study plan summary
        if result:
            with open("final_study_plan.md", "r") as f:
                study_plan_summary = f.read()
            return study_plan_summary
        else:
            return None
