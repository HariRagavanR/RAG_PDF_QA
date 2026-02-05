from sentence_transformers import SentenceTransformer
import numpy as np

model = SentenceTransformer("all-MiniLM-L6-v2")

sentences = [
    "Python developer with Flask experience",
    "Backend engineer skilled in APIs",
    "I like playing football"
]

embeddings = model.encode(sentences)

print("Embedding shape:", embeddings.shape)
print("First vector sample:", embeddings[0][:10])
