from sentence_transformers import SentenceTransformer
from app.config import EMBEDDING_MODEL_NAME

model = SentenceTransformer(EMBEDDING_MODEL_NAME)

def get_embedding(text: str):
    # Returns embedding as numpy array
    return model.encode([text])[0]

def get_embeddings(texts: list):
    return model.encode(texts)
