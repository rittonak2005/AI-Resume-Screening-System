import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=os.getenv("GOOGLE_API_KEY"),
    temperature=0
)


def ask_hr_chatbot(results, question):

    prompt = f"""
You are an expert HR Recruitment Assistant.

Below are the resume analysis results:

{results}

Answer the HR manager's question based ONLY on these results.

Question:
{question}
"""

    response = llm.invoke(prompt)

    return response.content