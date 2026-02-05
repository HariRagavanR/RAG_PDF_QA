from sentence_transformers import SentenceTransformer
import numpy as np

def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

model = SentenceTransformer("all-MiniLM-L6-v2")

texts = [
    "Python developer with Flask experience",
    "Backend engineer skilled in APIs",
    "I like playing football"
]

query = "Flask backend developer"

embeddings = model.encode(texts)
query_embedding = model.encode(query)

for text, emb in zip(texts, embeddings):
    score = cosine_similarity(query_embedding, emb)
    print(f"Similarity with '{text}': {score:.3f}")
