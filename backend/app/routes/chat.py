from fastapi import APIRouter
from app.models.request_models import ChatRequest
from app.models.response_models import ChatResponse
from app.services.rag_service import get_context_for_query
from app.services.groq_service import generate_answer

router = APIRouter()

@router.post("/ask", response_model=ChatResponse)
async def ask_question(request: ChatRequest):
    context = get_context_for_query(request.query)
    answer = generate_answer(request.query, context)
    return ChatResponse(answer=answer, context_used=context)
