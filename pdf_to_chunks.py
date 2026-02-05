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

if __name__ == "__main__":
    text = load_pdf_text("sample.pdf")
    chunks = chunk_text(text)

    print(f"Total chunks created: {len(chunks)}")
    print("Sample chunk:\n", chunks[0][:300])
