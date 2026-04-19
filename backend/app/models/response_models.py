from pydantic import BaseModel
from typing import List

class ChatResponse(BaseModel):
    answer: str
    context_used: List[str]

class QuizOption(BaseModel):
    id: str
    text: str

class QuizQuestion(BaseModel):
    id: str
    question: str
    options: List[QuizOption]
    correct_option_id: str

class QuizResponse(BaseModel):
    questions: List[QuizQuestion]
