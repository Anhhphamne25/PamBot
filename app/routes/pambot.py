from fastapi import APIRouter
from fastapi import HTTPException
from app.schemas.pambot_schema import PamBotRequest, PamBotResponse
from app.services.rag_service import generate_answer

router = APIRouter()

@router.post("/ask", response_model=PamBotResponse)
def ask_pambot(payload: PamBotRequest):
    try:
        answer = generate_answer(payload.question)

        return PamBotResponse(answer=answer)

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e),
        )