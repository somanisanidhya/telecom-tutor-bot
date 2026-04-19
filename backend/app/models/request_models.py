from pydantic import BaseModel

class ChatRequest(BaseModel):
    query: str

class QuizRequest(BaseModel):
    topic: str = "telecommunications"
