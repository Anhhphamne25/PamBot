from fastapi import APIRouter, HTTPException, Header, Depends

from app.config import settings
from app.schemas.pambot_schema import PamBotRequest, PamBotResponse
from app.services.rag_service import generate_answer


router = APIRouter()


def verify_api_key(x_app_api_key: str = Header(None, alias="X-APP-API-KEY")):
    if x_app_api_key != settings.APP_API_KEY:
        raise HTTPException(
            status_code=401,
            detail="Invalid API key",
        )


@router.post(
    "/ask",
    response_model=PamBotResponse,
    dependencies=[Depends(verify_api_key)],
)
def ask_pambot(payload: PamBotRequest):
    try:
        answer = generate_answer(payload.question)

        return PamBotResponse(answer=answer)

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e),
        )