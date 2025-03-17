from agno.agent import Agent
from agno.models.ollama import Ollama

def setup_agent(knowledge_base):
    """Create the Agent using Ollama's llama3.2 model and the knowledge base."""
    return Agent(
        name="Local RAG Agent",
        model=Ollama(id="llama3.2"),
        knowledge=knowledge_base,
    )