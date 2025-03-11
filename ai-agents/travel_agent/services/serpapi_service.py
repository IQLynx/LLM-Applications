from agno.tools.serpapi import SerpApiTools

def create_serpapi_tool(serp_api_key: str) -> SerpApiTools:
    """Create and return the SerpAPI tool."""
    return SerpApiTools(api_key=serp_api_key)