from agno.agent import Agent
from agno.models.google import Gemini
from composio_phidata import Action, ComposioToolSet


def create_google_sheets_agent(composio_api_key: str, gemini_api_key: str) -> Agent:
    composio_toolset = ComposioToolSet(api_key=composio_api_key)
    google_sheets_tool = composio_toolset.get_tools(actions=[Action.GOOGLESHEETS_SHEET_FROM_JSON])[0]

    google_sheets_agent = Agent(
        model=Gemini(api_key=gemini_api_key),
        tools=[google_sheets_tool],
        show_tool_calls=True,
        system_prompt="You are an expert at creating and updating Google Sheets. You will be given user information in JSON format, and you need to write it into a new Google Sheet.",
        markdown=True
    )
    return google_sheets_agent


def create_prompt_transformation_agent(gemini_api_key: str) -> Agent:
    return Agent(
        model=Gemini(api_key=gemini_api_key),
        system_message="""You are an expert at transforming detailed user queries into concise company descriptions.
Your task is to extract the core business/product focus in 3-4 words.

Examples:
Input: "Generate leads looking for AI-powered customer support chatbots for e-commerce stores."
Output: "AI customer support chatbots for e commerce"

Input: "Find people interested in voice cloning technology for creating audiobooks and podcasts"
Output: "voice cloning technology"

Input: "Looking for users who need automated video editing software with AI capabilities"
Output: "AI video editing software"

Input: "Need to find businesses interested in implementing machine learning solutions for fraud detection"
Output: "ML fraud detection"

Always focus on the core product/service and keep it concise but clear.""",
        markdown=True
    )