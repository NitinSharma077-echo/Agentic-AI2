from dotenv import load_dotenv
load_dotenv()

from crewai import Task
from agents.planner_agent import planner_agent

study_plan_task = Task(
    description=(
        "Using the researcher's findings, create a personalized 30-day study "
        "plan with weekly goals, daily learning tasks, and resource mapping."
    ),
    agent=planner_agent,
    expected_output="A complete 30-day structured study plan."
)
