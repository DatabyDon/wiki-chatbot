import os
import frontmatter

def load_wiki(wiki_path="wiki"):
    docs = []
    for root, dirs, files in os.walk(wiki_path):
        for file in files:
            if file.endswith(".md"):
                full_path = os.path.join(root, file)
                post = frontmatter.load(full_path)
                docs.append({
                    "title": file.replace(".md", ""),
                    "path": full_path,
                    "content": post.content
                })
    return docs

if __name__ == "__main__":
    docs = load_wiki()
    for doc in docs:
        print(f"Loaded: {doc['title']} — {len(doc['content'])} characters")