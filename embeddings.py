import os
from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAIEmbeddings

# Load environment variables
load_dotenv()

# Get API Key
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# Create Embedding Model
embedding_model = GoogleGenerativeAIEmbeddings(
    model="models/embedding-001",
    google_api_key=GOOGLE_API_KEY
)


def create_embedding(text):
    """
    Converts text into an AI embedding.
    """
    return embedding_model.embed_query(text)