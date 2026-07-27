from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from src.loader import load_wiki
from src.retriever import retrieve
from src.chat import chat

app = FastAPI()

docs = load_wiki()

class Query(BaseModel):
    question: str

@app.post("/chat")
def chat_endpoint(query: Query):
    relevant_docs = retrieve(query.question, docs)
    if not relevant_docs:
        return {"answer": "I couldn't find anything relevant in the wiki."}
    answer = chat(query.question, relevant_docs)
    return {"answer": answer}

app.mount("/", StaticFiles(directory="static", html=True), name="static")