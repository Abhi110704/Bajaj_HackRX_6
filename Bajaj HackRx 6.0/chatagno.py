from agno.agent import Agent 
from agno.models.groq import Groq
from agno.document.chunking.semantic import SemanticChunking
from agno.knowledge.pdf import PDFKnowledgeBase
from agno.embedder.sentence_transformer import SentenceTransformerEmbedder
from agno.vectordb.lancedb import LanceDb
from agno.vectordb.search import SearchType
import os
from dotenv import load_dotenv
load_dotenv()
# Initialize embedder
embedder = SentenceTransformerEmbedder()

# LanceDB Vector DB
vector_db = LanceDb(
    table_name="policies",
    uri="./temp/lancedb",  # Using relative path
    embedder=embedder,
    search_type=SearchType.hybrid,
)


knowledge_base = PDFKnowledgeBase(
    path="./docs/BAJA_HEALTH_POLICY.pdf",
    vector_db=vector_db,
    chunking_strategy=SemanticChunking(
        embedder=embedder 
)
)

policy_prompt = """
You are an Insurance Policy Analyzer. Analyze policy queries using ONLY the provided knowledge base.

RESPONSE RULES:
1. Parse the query to extract key details (age, procedure, location, policy duration, etc).
2. Use semantic understanding to find the most relevant clauses from the policy document.
3. Evaluate the rules/clauses to make a decision (approve/reject, payout amount, etc).
4. ALWAYS respond in this JSON structure:
{
    \"decision\": \"approved/rejected/yes/no\",
    \"amount\": 0,  // integer or null if not applicable
    \"justification\": \"One short sentence, under 20 words, starting with Yes/No/Approved/Rejected, referencing the clause(s)\",
    \"clause_reference\": \"clause number or section\"
}
IMPORTANT: The 'justification' must always start with Yes/No/Approved/Rejected, be under 20 words, and always mention the clause reference. Do NOT use any other keys or add any extra text.
If information is not in knowledge base, respond: {\"error\": \"Information not found in policy documents\"}
Keep responses under 20 words. Focus on facts only.
"""

agent = Agent(
    model=Groq(id="llama3-8b-8192"),
    knowledge=knowledge_base,
    instructions=[policy_prompt],
    search_knowledge=True,
    markdown=True,
    show_tool_calls=False,
)

# Test the agent with a query
# query = "is accident in case of Fractures and dislocations covered by policy?"
# response = agent.print_response(query)
# print(response)

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import uvicorn
from fastapi.responses import JSONResponse
import json
import re
import io
import sys

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class AskRequest(BaseModel):
    question: str

@app.post("/ask")
async def ask_question(req: AskRequest):
    buffer = io.StringIO()
    sys_stdout = sys.stdout
    sys.stdout = buffer
    try:
        agent.print_response(req.question)
        raw_response = buffer.getvalue()
    finally:
        sys.stdout = sys_stdout
    print("AGENT RAW RESPONSE:", repr(raw_response))

    # Remove ANSI color codes
    ansi_escape = re.compile(r'\x1B[@-_][0-?]*[ -/]*[@-~]')
    clean_response = ansi_escape.sub('', raw_response)

    # Remove box drawing characters and lines
    clean_response = re.sub(r'[\u2500-\u257F┃]+', '', clean_response)  # Unicode box drawing
    clean_response = re.sub(r'[┏━┓┃┗]+', '', clean_response)  # Extra safety for box chars
    clean_response = re.sub(r'\n+', '\n', clean_response)

    # Extract JSON object from the cleaned response (from first { to last })
    start = clean_response.find('{')
    end = clean_response.rfind('}')
    if start != -1 and end != -1 and end > start:
        json_str = clean_response[start:end+1]
        # Remove trailing commas before }
        json_str = re.sub(r',\s*}', '}', json_str)
        try:
            response_json = json.loads(json_str.replace("'", '"'))
            print("EXTRACTED JSON:", response_json)  # Log the parsed JSON
            if "coverage_status" in response_json:
                return JSONResponse(content={
                    "decision": "approved" if response_json["coverage_status"].lower() in ["yes", "approved"] else "rejected",
                    "amount": response_json.get("details", {}).get("amounts", {}).get("type", 0),
                    "justification": response_json.get("summary", ""),
                    "clause_reference": response_json.get("details", {}).get("clause", "")
                })
            return JSONResponse(content=response_json)
        except Exception:
            pass
    return JSONResponse(content={"error": "Invalid response from agent", "raw": clean_response})

if __name__ == "__main__":
    # For API mode
    uvicorn.run("chatagno:app", host="0.0.0.0", port=8000, reload=True)
