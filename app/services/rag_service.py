from app.services.embedding_service import create_embedding
from app.services.llm_service import ask_llm
from app.vectorstore.qdrant import search_similar
from app.utils.prompt_builder import build_pambot_prompt


def generate_answer(question: str) -> str:
    question_vector = create_embedding(question)

    results = search_similar(
        vector=question_vector,
        limit=5,
    )

    contexts = []

    for item in results:
        payload = item.payload or {}
        text = payload.get("text")

        if text:
            contexts.append(text)

    if not contexts:
        return "I don't have information about that."

    prompt = build_pambot_prompt(
        question=question,
        contexts=contexts,
    )

    answer = ask_llm(prompt)

    return answer