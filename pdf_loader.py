from pypdf import PdfReader

def load_pdf_text(pdf_path):
    reader = PdfReader(pdf_path)
    full_text = ""

    for page in reader.pages:
        full_text += page.extract_text() + "\n"

    return full_text


if __name__ == "__main__":
    text = load_pdf_text("sample.pdf")
    print(text[:1000])  # first 1000 chars only
