import requests
import json

def chat(query, docs):
    context = ""
    for doc in docs:
        context += f"\n[Source: {doc['path']}]\n{doc['content']}\n"

    prompt = f"""You are a helpful assistant for an internal company wiki.
Answer the question using only the wiki content provided below.
If the answer is not in the wiki, say so.
Always mention which source you used.

--- WIKI CONTEXT ---
{context}
---

Question: {query}
Answer:"""

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={"model": "mistral-small", "prompt": prompt, "stream": False}
    )

    return response.json()["response"]

if __name__ == "__main__":
    from loader import load_wiki
    from retriever import retrieve

    docs = load_wiki()
    query = "What are the data naming conventions?"
    relevant_docs = retrieve(query, docs)
    answer = chat(query, relevant_docs)
    print(answer)