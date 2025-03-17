from .vector_db import setup_vector_db
from .knowledge_base import setup_knowledge_base
from .agent import setup_agent
from .playground import setup_playground
from agno.playground import serve_playground_app

# Define the collection name for the vector database
collection_name = "thai-recipe-index"

# Set up the vector database
vector_db = setup_vector_db(collection_name)

# Set up the knowledge base
knowledge_base = setup_knowledge_base(vector_db)

# Load the knowledge base, comment out after the first run to avoid reloading
knowledge_base.load(recreate=True, upsert=True)

# Create the agent
agent = setup_agent(knowledge_base)

# Set up the Playground UI
app = setup_playground(agent)

# Run the Playground app
if __name__ == "__main__":
    serve_playground_app("local_rag_agent:app", reload=True)