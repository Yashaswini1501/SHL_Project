from dotenv import load_dotenv
import os

from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from app.retriever import search_assessments
# import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()


# genai.configure(
#     api_key=os.getenv("GEMINI_API_KEY")
# )
# print(os.getenv("GEMINI_API_KEY"))


# model = genai.GenerativeModel("gemini-pro")
app = FastAPI()

# ------------------------------
# Request Schema
# ------------------------------

class Message(BaseModel):
    role: str
    content: str

class ChatRequest(BaseModel):
    messages: List[Message]

# ------------------------------
# Health Endpoint
# ------------------------------

@app.get("/health")
def health():
    return {"status": "ok"}

# ------------------------------
# Chat Endpoint
# ------------------------------

@app.post("/chat")
def chat(request: ChatRequest):

    messages = request.messages

    latest_user_message = messages[-1].content
    

# ------------------------------
# Comparison Support
# ------------------------------

    if "difference" in latest_user_message.lower():

        return {
            "reply": "OPQ measures personality and behavioral style, while GSA focuses on cognitive and problem-solving abilities.",
            "recommendations": [],
            "end_of_conversation": False
    }

    # ------------------------------
    # Handle vague queries
    # ------------------------------

    if len(latest_user_message.split()) < 3:

        return {
            "reply": "Could you share more details about the role, skills, or assessment requirements?",
            "recommendations": [],
            "end_of_conversation": False
        }

    # ------------------------------
    # Off-topic protection
    # ------------------------------

    banned_topics = [
        "legal",
        "law",
        "aws certificate",
        "medical advice",
        "politics"
    ]

    for topic in banned_topics:

        if topic in latest_user_message.lower():

            return {
                "reply": "I can only help with SHL assessments.",
                "recommendations": [],
                "end_of_conversation": False
            }
# ------------------------------
# Refinement Handling
# ------------------------------

    conversation_text = " ".join(
        [m.content for m in messages]
)

    # ------------------------------
    # Retrieve assessments
    # ------------------------------

    results = search_assessments(
        conversation_text,
        top_k=5
    )

    recommendations = []

    for item in results:

        recommendations.append({
            "name": item["name"],
            "url": item["url"],
            "test_type": item["test_type"]
        })

    # ------------------------------
    # Create LLM prompt
    # ------------------------------

    recommendations = results

    reply_text = f"Recommended assessments found for: {latest_user_message}"

    return {
        "reply": reply_text,
        "recommendations": recommendations,
        "end_of_conversation": False
}