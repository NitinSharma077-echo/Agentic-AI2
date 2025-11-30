from dotenv import load_dotenv
load_dotenv()
from tasks.research_task import research_task
from tasks.study_plan_task import study_plan_task
import agents
import tasks

from crewai import Agent, Task, Crew
from crewai import LLM

# Use light model
llm = LLM(model="gpt-4o-mini")

def generate_study_plan(topic, hours):
    agent = Agent(
        role="Study Planner",
        goal="Generate a short, structured 30-day study plan.",
        backstory="You specialize in creating simple and concise study roadmaps.",
        llm=llm,
        verbose=False
    )

    task = Task(
        description=(
            f"Create a simple, clear 30-day study plan for learning {topic}. "
            f"The user studies {hours} hours per day. "
            f"Keep it concise. No long paragraphs. No research section."
        ),
        agent=agent,
        expected_output="Short 30-day learning plan in bullet points."
    )

    crew = Crew(
        agents=[agent],
        tasks=[task],
        verbose=False
    )

    result = crew.kickoff()
    return result

def run_pipeline(topic, hours):
    return generate_study_plan(topic, hours)
