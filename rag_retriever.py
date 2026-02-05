from sentence_transformers import SentenceTransformer
import numpy as np
from pypdf import PdfReader

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

if __name__ == "__main__":
    text = load_pdf_text("sample.pdf")
    chunks = chunk_text(text)

    model = SentenceTransformer("all-MiniLM-L6-v2")
    chunk_embeddings = model.encode(chunks)

    query = "Flask backend experience"
    query_embedding = model.encode(query)

    similarities = [
        cosine_similarity(query_embedding, emb)
        for emb in chunk_embeddings
    ]

    best_index = int(np.argmax(similarities))
    print("Best matching chunk:\n")
    print(chunks[best_index])
