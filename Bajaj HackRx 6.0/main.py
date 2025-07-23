# install chromadb - `pip install chromadb`

import asyncio
from agno.embedder.sentence_transformer import SentenceTransformerEmbedder
from agno.models.groq import Groq
from agno.agent import Agent
from agno.knowledge.pdf_url import PDFUrlKnowledgeBase
from agno.vectordb.chroma import ChromaDb
from dotenv import load_dotenv
load_dotenv()
# Initialize ChromaDB


# Create knowledge base
knowledge_base = PDFUrlKnowledgeBase(
    urls=["https://agno-public.s3.amazonaws.com/recipes/ThaiRecipes.pdf"],
    vector_db=vector_db,
)

# Create and use the agent
agent = Agent(model=Groq(id="llama3-8b-8192"),knowledge=knowledge_base, show_tool_calls=True)

if __name__ == "__main__":
    asyncio.run(knowledge_base.aload(recreate=False))

    # Create and use the agent
    asyncio.run(agent.aprint_response("How to make Tom Kha Gai", markdown=True))