# rag_core.py
import os
import numpy as np
from pypdf import PdfReader
from sentence_transformers import SentenceTransformer
from groq import Groq

# 🔥 LOAD MODEL ONCE (GLOBAL)
embedder = SentenceTransformer("all-MiniLM-L6-v2")

def load_pdf_text(pdf_path):
    reader = PdfReader(pdf_path)
    text = ""
    for page in reader.pages:
        if page.extract_text():
            text += page.extract_text() + "\n"
    return text

def chunk_text(text, chunk_size=500, overlap=50):
    chunks = []
    start = 0
    while start < len(text):
        end = start + chunk_size
        chunks.append(text[start:end])
        start = end - overlap
    return chunks

def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

def answer_from_pdf(pdf_path, question, api_key):
    text = load_pdf_text(pdf_path)
    chunks = chunk_text(text)

    chunk_embeddings = embedder.encode(chunks)
    query_embedding = embedder.encode(question)

    sims = [cosine_similarity(query_embedding, e) for e in chunk_embeddings]
    TOP_K = 3
    top_k_indices = np.argsort(sims)[-TOP_K:][::-1]

    context = "\n\n".join([chunks[i] for i in top_k_indices])

    client = Groq(api_key=api_key)
    resp = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
              "role": "system",
              "content": (
                "You are a document-based assistant. "
                "Answer ONLY using the provided context. "
                "If not found, say: 'Not found in the document.'"
              )
            },
            {
              "role": "user",
              "content": f"Context:\n{context}\n\nQuestion: {question}"
            }
        ]
    )

    return resp.choices[0].message.content
