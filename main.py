from dotenv import load_dotenv
load_dotenv()

from crewai import Crew
from dotenv import load_dotenv
import os

from tasks.research_task import research_task
from tasks.study_plan_task import study_plan_task

load_dotenv()  # Load API key

def generate_study_plan(topic, hours):
    # Update tasks dynamically
    research_task.description = (
        f"Research the best resources for learning {topic}. "
        f"Consider that the user can study {hours} hours per day."
    )

    study_plan_task.description = (
        f"Using the research findings, create a structured 30-day study plan "
        f"for the topic: {topic}, with daily {hours} hours of study."
    )

    crew = Crew(
        agents=[
            research_task.agent,
            study_plan_task.agent
        ],
        tasks=[research_task, study_plan_task],
        verbose=True
    )

    return crew.kickoff()



# ------------- ADD THIS FOR FLASK ------------------

def run_pipeline(topic, hours):
    """Function Flask will call."""
    return generate_study_plan(topic, hours)

# ---------------------------------------------------


if __name__ == "__main__":
    print("\n==== STUDY PLAN GENERATOR ====")
    topic = input("Enter topic to study (e.g., Python, SQL, ML): ")
    hours = input("How many hours can you study per day? ")

    final_plan = generate_study_plan(topic, hours)
    print("\n=========== FINAL 30-DAY STUDY PLAN ===========\n")
    print(final_plan)
