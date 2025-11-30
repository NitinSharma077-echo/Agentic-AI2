from dotenv import load_dotenv
load_dotenv()

from crewai import Agent

planner_agent = Agent(
    role="Study Plan Designer",
    goal="Create a personalized study plan based on user goals and research data",
    backstory="You create structured study routines.",
    verbose=False
)
