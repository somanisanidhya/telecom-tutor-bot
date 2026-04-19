import os
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.environ.get("GROQ_API_KEY")
MODEL_NAME = os.environ.get("MODEL_NAME", "llama-3.3-70b-versatile")
DATA_PATH = os.path.join(os.path.dirname(__file__), "..", "..", "data", "telecom_docs.txt")
FAISS_INDEX_PATH = os.path.join(os.path.dirname(__file__), "db", "faiss_index.index")
EMBEDDING_MODEL_NAME = "all-MiniLM-L6-v2"