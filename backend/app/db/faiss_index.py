import faiss
import numpy as np
import os
from app.db.data_loader import telecom_chunks
from app.utils.embeddings import get_embeddings, get_embedding
from app.config import FAISS_INDEX_PATH

index = None

def build_index():
    global index
    if not telecom_chunks:
        print("No documents found to build index.")
        return

    embeddings = get_embeddings(telecom_chunks)
    dimension = embeddings.shape[1]
    
    index = faiss.IndexFlatL2(dimension)
    index.add(np.array(embeddings).astype('float32'))
    
    faiss.write_index(index, FAISS_INDEX_PATH)
    print("FAISS index built and saved successfully.")

def load_or_build_index():
    global index
    if os.path.exists(FAISS_INDEX_PATH):
        index = faiss.read_index(FAISS_INDEX_PATH)
        print("Loaded FAISS index from disk.")
    else:
        build_index()

def search_index(query: str, k: int = 3):
    global index
    if index is None:
        load_or_build_index()
    
    query_embedding = get_embedding(query).astype('float32').reshape(1, -1)
    distances, indices = index.search(query_embedding, k)
    
    results = []
    for idx in indices[0]:
        if 0 <= idx < len(telecom_chunks):
            results.append(telecom_chunks[idx])
    return results

# Initialize on import
load_or_build_index()
