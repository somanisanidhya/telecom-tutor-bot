import os
from app.config import DATA_PATH

def load_and_chunk_data():
    if not os.path.exists(DATA_PATH):
        return []
    
    with open(DATA_PATH, 'r', encoding='utf-8') as f:
        content = f.read()

    # Simple paragraph-based chunking
    chunks = [c.strip() for c in content.split('\n') if len(c.strip()) > 10]
    return chunks

telecom_chunks = load_and_chunk_data()
