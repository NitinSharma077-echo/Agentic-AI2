from dotenv import load_dotenv
load_dotenv()

from crewai import Agent

researcher_agent = Agent(
    role="Subject Research Specialist",
    goal="Research and gather study resources for the chosen topic",
    backstory=(
        "You are an expert researcher who collects high-quality books, videos, "
        "courses, and free resources from across the web."
    ),
    verbose=True
)
