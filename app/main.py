from fastapi import FastAPI
from app.routes.pambot import router as pambot_router

app = FastAPI(
    title = "PamBot",
    description = "PamBot is a chatbot that can answer questions about the Pam information and Pam's project.",
    version = "1.0.0",
)

app.include_router(pambot_router, prefix="/pambot", tags=["PamBot"])

@app.get("/")
def root():
    return {"message": "Welcome to PamBot! Ask me anything about Pam and her project."}

@app.get("/health")
def health():
    return {"status": "ok"}

