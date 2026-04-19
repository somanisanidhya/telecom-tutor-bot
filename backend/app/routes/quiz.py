from fastapi import APIRouter
from app.models.request_models import QuizRequest
from app.models.response_models import QuizResponse
from app.services.quiz_service import generate_quiz

router = APIRouter()

@router.post("/quiz", response_model=QuizResponse)
async def get_quiz(request: QuizRequest):
    questions = generate_quiz(topic=request.topic)
    return QuizResponse(questions=questions)
