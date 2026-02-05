from pypdf import PdfReader
from sentence_transformers import SentenceTransformer
from groq import Groq
from dotenv import load_dotenv
import numpy as np
import os

load_dotenv()

# ---------- Helpers ----------
def load_pdf_text(pdf_path):
    reader = PdfReader(pdf_path)
    text = ""
    for page in reader.pages:
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

# ---------- Main ----------
if __name__ == "__main__":
    pdf_path = "sample.pdf"
    question = input("Ask a question from the PDF: ")

    text = load_pdf_text(pdf_path)
    chunks = chunk_text(text)

    embedder = SentenceTransformer("all-MiniLM-L6-v2")
    chunk_embeddings = embedder.encode(chunks)
    query_embedding = embedder.encode(question)

    similarities = [
        cosine_similarity(query_embedding, emb)
        for emb in chunk_embeddings
    ]

    best_chunk = chunks[int(np.argmax(similarities))]

    client = Groq(api_key=os.getenv("GROQ_API_KEY"))

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                "role": "system",
                "content": "Answer ONLY from the given context. If answer not found, say 'Not found in document.'"
            },
            {
                "role": "user",
                "content": f"Context:\n{best_chunk}\n\nQuestion: {question}"
            }
        ]
    )

    print("\n🤖 Answer:\n", response.choices[0].message.content)
