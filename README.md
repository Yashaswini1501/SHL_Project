# SHL Assessment Recommendation Chatbot

## Project Overview

This project is an AI-powered SHL Assessment Recommendation Chatbot built using FastAPI, Sentence Transformers, and FAISS.

The chatbot helps recruiters or hiring managers find suitable SHL assessments based on job requirements, skills, personality traits, and refinement queries.

The system supports:

* Assessment recommendation retrieval
* Conversation refinement handling
* Comparison queries
* FastAPI REST API endpoints
* Semantic search using embeddings
* Swagger API testing

---

# Features

## 1. Semantic Assessment Retrieval

The chatbot uses Sentence Transformers embeddings and FAISS vector search to retrieve the most relevant assessments.

---

## 2. Refinement Handling

The chatbot remembers previous conversation context.

Example:

User: Hiring a software engineer

User: Add personality tests

The chatbot combines both queries and returns refined recommendations.

---

## 3. Comparison Queries

The chatbot can answer simple comparison questions.

Example:

* Difference between OPQ and GSA

---

## 4. FastAPI Backend

The project exposes REST APIs using FastAPI.

---

## 5. Swagger API Testing

Interactive API testing available through Swagger UI.

---

# Tech Stack

* Python
* FastAPI
* Uvicorn
* Sentence Transformers
* FAISS
* NumPy
* Pydantic
* JSON

---

# Project Structure

```bash
SHL_Project/
│
├── app/
│   └── retriever.py
│
├── data/
│   └── catalog.json
│
├── venv/
│
├── .env
├── .gitignore
├── main.py
├── README.md
├── requirements.txt
```

---

# Installation Steps

## Step 1: Clone Repository

```bash
git clone <your-github-repository-url>
```

---

## Step 2: Open Project

```bash
cd SHL_Project
```

---

## Step 3: Create Virtual Environment

```bash
python -m venv venv
```

---

## Step 4: Activate Virtual Environment

### Windows

```bash
venv\Scripts\activate
```

### Mac/Linux

```bash
source venv/bin/activate
```

---

## Step 5: Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Running the Application

Start the FastAPI server:

```bash
uvicorn main:app --reload
```

---

# Swagger Documentation

Open browser:

```bash
http://127.0.0.1:8000/docs
```

---

# API Endpoints

## Health Endpoint

### GET `/health`

Checks whether API is running.

### Example Response

```json
{
  "status": "ok"
}
```

---

## Chat Endpoint

### POST `/chat`

Returns recommended SHL assessments.

---

# Example Request

```json
{
  "messages": [
    {
      "role": "user",
      "content": "Hiring a Java developer with communication skills"
    }
  ]
}
```

---

# Example Response

```json
{
  "reply": "Recommended assessments found for: Hiring a Java developer with communication skills",
  "recommendations": [
    {
      "name": "Java Test",
      "url": "https://www.shl.com",
      "test_type": "K"
    },
    {
      "name": "OPQ32r",
      "url": "https://www.shl.com",
      "test_type": "P"
    }
  ],
  "end_of_conversation": false
}
```

---

# Refinement Query Example

## Request

```json
{
  "messages": [
    {
      "role": "user",
      "content": "Hiring a software engineer"
    },
    {
      "role": "assistant",
      "content": "Any additional requirements?"
    },
    {
      "role": "user",
      "content": "Add personality tests"
    }
  ]
}
```

---

# Comparison Query Example

## Request

```json
{
  "messages": [
    {
      "role": "user",
      "content": "Difference between OPQ and GSA"
    }
  ]
}
```

---

# Embedding and Retrieval Workflow

1. Assessment descriptions are stored in `catalog.json`
2. Sentence Transformers converts descriptions into embeddings
3. FAISS indexes embeddings
4. User query is converted into embedding
5. Semantic similarity search retrieves relevant assessments

---

# Future Improvements

* Add real SHL catalog scraping
* Add LLM-generated conversational responses
* Add frontend UI
* Add database integration
* Add authentication
* Improve comparison generation
* Add deployment monitoring

---

# Deployment

The project can be deployed using:

* Render
* Railway
* AWS
* Azure
* Google Cloud

---

# Render Deployment Steps

## Build Command

```bash
pip install -r requirements.txt
```

## Start Command

```bash
uvicorn main:app --host 0.0.0.0 --port 10000
```

---

# Environment Variables

Create a `.env` file:

```env
GEMINI_API_KEY=your_api_key
```

---

# .gitignore

```bash
venv/
.env
__pycache__/
```

---

# Author

Abhi Ram

---

# Conclusion

This project demonstrates the implementation of an AI-powered assessment recommendation system using semantic search and FastAPI.

The chatbot supports intelligent retrieval, refinement handling, and scalable API-based architecture suitable for recruitment and talent assessment workflows.
