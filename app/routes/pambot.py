from fastapi import APIRouter
from app.schemas.pambot_schema import PamBotRequest, PamBotResponse

router = APIRouter()

@router.post("/ask", response_model=PamBotResponse)
def ask_pambot(payload: PamBotRequest):
    question = payload.question
    return PamBotResponse(
        answer=f"PamBot received your question: {question}"
    )
