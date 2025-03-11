from agno.agent import Agent
from agno.models.google import Gemini
from utils.text_utils import dedent

def create_planner_agent(gemini_api_key: str) -> Agent:
    """Create and return the Planner agent."""
    return Agent(
        name="Planner",
        role="Generates a draft itinerary based on user preferences and research results",
        model=Gemini(api_key=gemini_api_key),
        description=dedent(
            """\
        You are a senior travel planner. Given a travel destination, the number of days the user wants to travel for, and a list of research results,
        your goal is to generate a draft itinerary that meets the user's needs and preferences.
        """
        ),
        instructions=[
            "Given a travel destination, the number of days the user wants to travel for, and a list of research results, generate a draft itinerary that includes suggested activities and accommodations.",
            "Ensure the itinerary is well-structured, informative, and engaging.",
            "Ensure you provide a nuanced and balanced itinerary, quoting facts where possible.",
            "Remember: the quality of the itinerary is important.",
            "Focus on clarity, coherence, and overall quality.",
            "Never make up facts or plagiarize. Always provide proper attribution.",
        ],
        add_datetime_to_instructions=True,
    )