# IntelliClause: Document Q&A (HackRx 6.0 Submission)

## Overview
IntelliClause is an AI-powered system that uses Large Language Models (LLMs) to process natural language queries and retrieve relevant information from large, unstructured documents such as policy documents, contracts, and emails.

## Features
- **Multi-file support:** Upload and analyze PDFs, Word (.docx), and Email (.eml) files.
- **Semantic search:** Finds relevant clauses using embeddings, not just keyword search.
- **Natural language Q&A:** Handles vague, shorthand, or plain English queries.
- **Structured JSON output:** Always returns decision, amount, justification, and clause reference.
- **Explainable answers:** Every answer references the exact clause used.
- **Modern, responsive frontend:** Clean UI, works on desktop and mobile.
- **Hackathon-ready:** Robust, extensible, and easy to demo.

## How to Run
1. **Clone the repository and navigate to the project folder:**
   ```sh
   git clone <your-repo-url>
   cd hackrx/policyai
   ```
2. **Install Python 3.12** (if not already installed)
3. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```
4. **Set your GROQ_API_KEY in a `.env` file:**
   ```env
   GROQ_API_KEY=your_actual_groq_api_key_here
   ```
5. **Start the backend:**
   ```sh
   python chatagno.py
   ```
6. **Start the frontend (in the same folder):**
   ```sh
   python -m http.server 8080
   # Then open http://localhost:8080/Index.html in your browser
   ```
7. **Upload your documents and ask questions!**

## How It Works
1. **Upload Documents:** Drag and drop or select PDF, DOCX, or EML files.
2. **Ask a Question:** Enter a query in plain English (e.g., `46M, knee surgery, Pune, 3-month policy`).
3. **Get an Answer:**
   - One-line summary (e.g., `Approved under Clause 4.3: Pre-scheduled surgeries`)
   - Structured details (decision, amount, clause reference)

## Example
**Query:**
```
Knee surgery covered?
```
**Answer:**
```
Approved under clause 3.4. Knee surgery is a covered procedure.
Decision: approved
Amount: 0
Clause Reference: 3.4
```

## For Hackathon Judges
- Works with all file types (PDF, DOCX, EML)
- Handles vague, incomplete, or plain English queries
- Always references the correct clause
- JSON output is ready for audit, automation, or downstream use
- Modern, user-friendly UI

## Applications
- Insurance claim processing
- Legal compliance
- Human resources
- Contract management

## Team
Team: HackerXHacker
- Abhiyanshu Anand
- Sanskar Singh
- Harsh Katiyar
- Siddharth Tripathi
- Abhishek Singh

---
**Ready for HackRx 6.0!**