from agno.vectordb.qdrant import Qdrant
from agno.embedder.ollama import OllamaEmbedder

def setup_vector_db(collection_name):
    """Set up Qdrant as the vector database."""
    return Qdrant(
        collection=collection_name,
        url="http://localhost:6333/",
        embedder=OllamaEmbedder()
    )