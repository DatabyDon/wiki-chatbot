def retrieve(query, docs, top_n=2):
    query_tokens = query.lower().split()
    scored = []
    for doc in docs:
        score = sum(1 for token in query_tokens if token in doc["content"].lower())
        scored.append((score, doc))
    scored.sort(key=lambda x: x[0], reverse=True)
    return [doc for score, doc in scored[:top_n] if score > 0]

if __name__ == "__main__":
    from loader import load_wiki
    docs = load_wiki()
    results = retrieve("what are the data naming conventions?", docs)
    for r in results:
        print(f"Match: {r['title']}")
        print(r['content'][:200])
        print("---")