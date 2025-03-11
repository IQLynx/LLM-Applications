from agno.agent import Agent
from agno.models.google import Gemini
from agno.knowledge.pdf_url import PDFUrlKnowledgeBase
from agno.vectordb.lancedb import LanceDb, SearchType
from agno.playground import Playground, serve_playground_app
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.embedder.google import GeminiEmbedder
import uvicorn

db_uri = "tmp/lancedb"
# Create a knowledge base from a PDF
knowledge_base = PDFUrlKnowledgeBase(
    urls=["https://phi-public.s3.amazonaws.com/recipes/ThaiRecipes.pdf"],
    # Use LanceDB as the vector database
    vector_db=LanceDb(table_name="recipes",
                      uri=db_uri,
                      search_type=SearchType.vector,
                      embedder=GeminiEmbedder(api_key="AIzaSyCpHa6CM4eBSklUKk9fVZBv5KraCifyQZ4")),
)
# Load the knowledge base: Comment out after first run
knowledge_base.load(upsert=True)

rag_agent = Agent(
    model=Gemini(api_key="AIzaSyCpHa6CM4eBSklUKk9fVZBv5KraCifyQZ4"),
    agent_id="rag-agent",
    knowledge=knowledge_base, # Add the knowledge base to the agent
    tools=[DuckDuckGoTools()],
    show_tool_calls=True,
    markdown=True,
)

app = Playground(agents=[rag_agent]).get_app()

if __name__ == "__main__":
    serve_playground_app("rag_agent:app", reload=True)