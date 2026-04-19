from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes.chat import router as chat_router
from app.routes.quiz import router as quiz_router
from app.routes.health import router as health_router
import app.db.faiss_index  # Need this to initialize index on startup

app = FastAPI(title="Telecom Tutor Bot API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(health_router, tags=["Health"])
app.include_router(chat_router, tags=["Chat"])
app.include_router(quiz_router, tags=["Quiz"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
