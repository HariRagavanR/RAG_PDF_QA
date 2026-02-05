def chunk_text(text, chunk_size=500, overlap=50):
    chunks = []
    start = 0

    while start < len(text):
        end = start + chunk_size
        chunk = text[start:end]
        chunks.append(chunk)
        start = end - overlap  # overlap for context

    return chunks


if __name__ == "__main__":
    sample_text = "This is a sample text. " * 200
    chunks = chunk_text(sample_text)

    print(f"Total chunks: {len(chunks)}")
    print(chunks[0][:200])
