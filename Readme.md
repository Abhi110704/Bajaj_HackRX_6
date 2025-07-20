# IntelliClause: LLM-Powered Intelligent Query–Retrieval System

## HackRx 6.0 Hackathon Submission

- **Hackathon:** HackRx 6.0
- **Organized By:** Bajaj Finserv Health Limited
- **Theme:** Generative AI

---

## Team Details

- **Team Name:** HackerXHacker
- **Team Members:**
    - Abhiyanshu Anand
    - Sanskar Singh
    - Harsh Katiyar
    - Siddharth Tripathi
    - Abhishek Singh

---

## 1. Problem Statement

Build a system that leverages Large Language Models (LLMs) to process natural language queries and retrieve relevant information from large, unstructured documents such as policy documents, contracts, and emails. The system must be able to interpret vague or shorthand queries, perform semantic retrieval, evaluate information based on document clauses, and return clear, justified decisions.

---

## 2. Project Description: IntelliClause

**IntelliClause** is a fully functional web application that serves as an AI-powered assistant for analyzing complex documents. It provides a clean, user-friendly interface where users can upload multiple PDF documents (such as insurance policies) and ask questions in plain English. The application leverages a powerful Large Language Model (LLM) to read, understand, and reason about the content of the documents, providing direct, accurate, and justifiable answers.

This project directly addresses the hackathon's challenge by creating a practical tool that transforms the tedious task of manual document review into an instant, intelligent Q&A session.

### How It Works

The application operates through a seamless client-side and server-side workflow:

1. **Document Upload & Processing (Client-Side):** Users upload one or more PDF files via a simple drag-and-drop interface. The application uses the `pdf.js` library to extract all text from the documents directly within the user's browser, ensuring data privacy as the original files are never sent to a server.
2. **Query Submission (Client-Side):** Users ask questions in the text area, using either full sentences or shorthand queries.
3. **API Call to LLM (Backend Communication):** The application packages the extracted text from all documents (as context) and the user's query into a carefully engineered prompt, then sends this information to the Google Gemini LLM via an API call.
4. **AI Analysis & Decision (Server-Side):** The LLM receives the context and query, then:
    - **Parses the Query:** Interprets the user's intent, even from shorthand notes.
    - **Semantic Retrieval:** Scans the provided document text to find the most relevant clauses.
    - **Evaluation:** Applies the rules and conditions from the clauses to the facts of the query scenario.
    - **Response Generation:** Formulates a concise, direct answer based on its analysis, citing the source document for transparency.
5. **Displaying the Answer (Client-Side):** The application receives the AI's response and displays it clearly in the "Answer" section for the user.

### Key Features

- **Intuitive User Interface:** Modern, responsive, and visually appealing single-page application.
- **Multi-PDF Upload:** Supports uploading and analyzing multiple documents simultaneously.
- **Client-Side Text Extraction:** Ensures user privacy by processing PDFs in the browser.
- **Robust AI Engine:** Capable of understanding natural language and shorthand queries.
- **Accurate & Justified Answers:** Provides clear "Yes/No" decisions with explanations and source citations.
- **Fully Dynamic:** Every answer is generated based on the uploaded documents; no hardcoded responses.

### Technology Stack

- **Frontend:** HTML5, Tailwind CSS
- **JavaScript Libraries:**
    - `pdf.js` for client-side PDF text extraction
    - `lucide-icons` for modern, clean icons
- **Backend AI Model:** Google Gemini 2.0 Flash (accessed via API)

---

## 3. How to Run the Project

The entire application is self-contained in a single `index.html` file.

1. **Save the File:** Save the provided HTML code as `index.html`.
2. **Open in Browser:** Open the `index.html` file in any modern web browser (e.g., Google Chrome, Mozilla Firefox, Microsoft Edge).
3. **That's It!** The application will be running locally on your machine.

---

## 4. HackRx 6.0 Hackathon Information

### About HackRx 6.0

HackRx is the annual flagship hackathon organized by Bajaj Finserv Health Limited, designed exclusively for engineering students across India. It offers a dynamic platform for the brightest tech minds to compete, collaborate, and create impactful solutions. Participants are mentored by top industry leaders as they work on real-world problem statements sponsored by the Bajaj Finserv Group.

This year, HackRx 6.0 dives into the exciting world of Generative AI. Participants are challenged to design an LLM-powered intelligent query–retrieval system capable of handling large documents and making smart, contextual inferences, just like a human.

### Competition Structure

- **Registrations:** Teams of 2-5 members register for the hackathon.
- **Deepdive Webinar:** A webinar provides insights into the theme and problem statement.
- **Pitch Deck & Code Submission:** Teams submit a pitch deck and their code for the preliminary round.
- **Online Evaluation:** Submissions are evaluated, and a live leaderboard tracks team rankings.
- **Grand Finale:** Shortlisted teams present their fully developed solutions to a panel of judges.

---
