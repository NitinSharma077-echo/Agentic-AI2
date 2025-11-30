from dotenv import load_dotenv
load_dotenv()

from crewai import Task
from agents.researcher_agent import researcher_agent

research_task = Task(
    description=(
        "Research the topic thoroughly. Include books, videos, online courses, "
        "blogs, free resources, and beginner-to-advanced learning paths."
    ),
    agent=researcher_agent,
    expected_output="A structured research summary with top resources."
)
