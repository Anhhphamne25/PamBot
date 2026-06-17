from pydantic import BaseModel, Field

class PamBotRequest(BaseModel):
    question: str = Field(..., min_length=2, description="The question to be processed by PamBot")

class PamBotResponse(BaseModel):
    answer: str = Field(..., description="The answer provided by PamBot")
