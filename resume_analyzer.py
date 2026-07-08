import os
import json
import re
import streamlit as st
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

# -------------------------------
# Load Environment Variables
# -------------------------------
load_dotenv()

# -------------------------------
# Gemini Model
# -------------------------------
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=os.getenv("GOOGLE_API_KEY"),
    temperature=0
)


def analyze_resume(resume_text, job_description):

    # -------------------------------
    # Empty Resume Check
    # -------------------------------
    if not resume_text.strip():
        return {
            "match_score": 0,
            "matching_skills": [],
            "missing_skills": [],
            "strengths": [],
            "weaknesses": ["Resume contains no readable text."],
            "recommendation": "Not Recommended"
        }

    # -------------------------------
    # Prompt
    # -------------------------------
    prompt = f"""
You are an experienced HR Recruiter.

Compare the following resume with the given job description.

Resume:
{resume_text}

Job Description:
{job_description}

IMPORTANT RULES:

Return ONLY valid JSON.

Do NOT write explanations.
Do NOT use markdown.
Do NOT use ```json.

Return exactly like this:

{{
    "match_score": 85,
    "matching_skills": ["Python","SQL"],
    "missing_skills": ["Power BI"],
    "strengths": ["Strong analytical skills"],
    "weaknesses": ["No Power BI experience"],
    "recommendation": "Recommended"
}}
"""

    try:

        response = llm.invoke(prompt)

        content = response.content.strip()

        # Empty Response
        if not content:
            raise ValueError("Gemini returned an empty response.")

        # Remove Markdown
        content = content.replace("```json", "")
        content = content.replace("```", "")
        content = content.strip()

        # Extract JSON
        match = re.search(r"\{.*\}", content, re.DOTALL)

        if not match:
            raise ValueError("No valid JSON found in Gemini response.")

        json_text = match.group()

        # Convert JSON to Dictionary
        analysis = json.loads(json_text)

        # Default Values
        analysis.setdefault("match_score", 0)
        analysis.setdefault("matching_skills", [])
        analysis.setdefault("missing_skills", [])
        analysis.setdefault("strengths", [])
        analysis.setdefault("weaknesses", [])
        analysis.setdefault("recommendation", "Not Available")

        return analysis

    except Exception as e:

        st.error(f"❌ Gemini Error: {e}")

        return {
            "match_score": 0,
            "matching_skills": [],
            "missing_skills": [],
            "strengths": [],
            "weaknesses": ["AI analysis failed."],
            "recommendation": "Not Available"
        }