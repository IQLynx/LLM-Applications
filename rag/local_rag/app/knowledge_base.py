from agno.knowledge.pdf_url import PDFUrlKnowledgeBase

def setup_knowledge_base(vector_db):
    """Set up the knowledge base with the specified PDF URL."""
    return PDFUrlKnowledgeBase(
        urls=["https://phi-public.s3.amazonaws.com/recipes/ThaiRecipes.pdf"],
        vector_db=vector_db,
    )