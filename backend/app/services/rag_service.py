from app.db.faiss_index import search_index

def get_context_for_query(query: str, k: int = 3):
    return search_index(query, k)
