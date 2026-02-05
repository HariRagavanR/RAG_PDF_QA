# RAG – PDF Question Answering System

A complete **Retrieval-Augmented Generation (RAG)** system built using Python to answer questions **directly from PDF documents** with high accuracy and minimal hallucination.

This project demonstrates **company-level GenAI architecture** used in internal knowledge bases, document assistants, and AI-powered search systems.

---

## 🚀 What This Project Does

- Loads and reads PDF documents
- Splits text into overlapping chunks
- Converts chunks into semantic embeddings
- Retrieves the most relevant content based on a user query
- Uses an LLM to generate answers **strictly from the retrieved document context**

> No guessing. No hallucination. Only document-grounded answers.

---

## 🧠 RAG Architecture (High Level)

PDF Document
↓
Text Extraction
↓
Chunking (with overlap)
↓
Embeddings (Semantic Vectors)
↓
Similarity Search (Retriever)
↓
LLM Answer Generation (Context-Aware)


---

## 🛠️ Tech Stack

- **Python**
- **sentence-transformers** (semantic embeddings)
- **Groq LLM API**
- **NumPy** (cosine similarity)
- **PyPDF** (PDF text extraction)

---

## 📂 Project Structure

rag-pdf-question-answering/
├── rag_qa.py # End-to-end RAG Q&A pipeline
├── rag_retriever.py # Semantic retrieval logic
├── pdf_loader.py # PDF text extraction
├── pdf_to_chunks.py # PDF to chunk conversion
├── chunker.py # Chunking with overlap
├── requirements.txt
└── README.md


---

## ▶️ How to Run

1. Clone the repository
2. Create and activate a virtual environment
3. Install dependencies:

pip install -r requirements.txt


4. Add your Groq API key in a `.env` file:

GROQ_API_KEY=your_api_key_here


5. Run the RAG system:

python rag_qa.py


6. Ask questions based on the PDF content.

---

## 🧪 Example Questions

- What role is mentioned in the document?
- What backend technologies are listed?
- What skills are highlighted?
- What experience is mentioned about Flask?

---

## 🎯 Key Learnings & Highlights

- Built a full **RAG pipeline from scratch**
- Implemented **semantic search** using embeddings
- Reduced hallucinations using strict context control
- Understood the difference between **chatbots vs document-grounded AI**
- Gained hands-on experience with real GenAI system design

---

## 🔐 Security & Best Practices

- API keys handled via environment variables
- No sensitive data committed to GitHub
- Clean, modular, and readable code
- CPU-only embedding setup (cost-efficient)

---

## 🔮 Future Improvements

- Flask-based Web UI (PDF upload + Q&A)
- Top-k chunk retrieval for better accuracy
- Vector database integration (FAISS / Chroma)
- Caching embeddings for performance
- Multi-PDF support

---

## 👨‍💻 About the Author

**Hari Ragavendiran R**  
Final-year ECE student | Aspiring GenAI Engineer  
Focused on building **real-world GenAI & backend systems**

GitHub: https://github.com/HariRagavanR  
LinkedIn: https://www.linkedin.com/in/hari-ragavendiran-r-a61679259

---

> **Learning philosophy:**  
> _If AI answers confidently, the engineer must verify intelligently._
