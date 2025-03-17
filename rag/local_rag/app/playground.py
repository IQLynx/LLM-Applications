from agno.playground import Playground

def setup_playground(agent):
    """Set up the Playground UI for the RAG agent."""
    return Playground(agents=[agent]).get_app()