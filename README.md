# 📄 DocuMind AI – PDF Question Answering using RAG

DocuMind AI is a **Generative AI web application** built using a **Retrieval-Augmented Generation (RAG)** architecture.  
It allows users to upload a PDF document and ask natural language questions, with answers generated **strictly from the document content**.

This project demonstrates **end-to-end GenAI system design**, from local development to cloud deployment and real-world production debugging.

<img width="1920" height="1080" alt="Screenshot at 2026-02-05 18-24-13" src="https://github.com/user-attachments/assets/b253b5e6-6414-4ba7-b4aa-b2ede71baa41" />
<img width="1920" height="1080" alt="Screenshot at 2026-02-05 18-23-26" src="https://github.com/user-attachments/assets/2e858880-6601-4484-a741-b22862954396" />
<img width="1920" height="1080" alt="Screenshot at 2026-02-05 18-23-01" src="https://github.com/user-attachments/assets/1f0398a4-9d22-4675-9b19-7bdb1e6a1760" />
<img width="1920" height="1080" alt="Screenshot at 2026-02-05 18-22-25" src="https://github.com/user-attachments/assets/c8e1b26f-08d5-4d06-94b4-cb87ae09c87a" />
<img width="1920" height="1080" alt="Screenshot at 2026-02-05 18-22-06" src="https://github.com/user-attachments/assets/1f97cc9c-2a56-43bf-92b5-dff30f306d4b" />


---

## 🚀 Features
- Upload a PDF once per session
- Ask **multiple questions interactively** without re-uploading
- Context-aware answers using RAG (no hallucinations)
- Session-isolated usage (safe for multiple users)
- Clean, modern UI
- Deployed on cloud (Render)

---

## 🧠 How It Works (RAG Flow)
1. PDF is uploaded and stored per user session  
2. Document text is extracted and chunked  
3. Relevant chunks are retrieved based on semantic similarity  
4. Retrieved context is passed to an LLM  
5. Final answer is generated **only from document context**

---

## 🛠️ Tech Stack
- **Python**
- **Flask**
- **RAG Architecture**
- **Sentence Transformers (Embeddings)**
- **Groq LLM API**
- **HTML, CSS**
- **Render (Deployment)**

---

## 🌐 Live Demo
👉 https://documind-ai-ap3x.onrender.com

---

## 📂 Project Structure
```
RAG_PDF_QA/
├── app.py                 # Flask application & session handling
├── rag_core.py            # Core RAG logic
├── pdf_loader.py          # PDF text extraction
├── chunker.py             # Text chunking logic
├── embedding_text.py      # Embedding utilities
├── rag_retriever.py       # Similarity & retrieval logic
├── templates/
│   └── index.html         # UI template
├── static/
│   ├── style.css          # Styling
│   └── bg.jpg             # Background image
├── uploads/               # Session-based uploaded PDFs
├── requirements.txt
└── README.md
```

---

## ⚙️ Key Engineering Learnings
- Implementing **session-based state management** in Flask
- Handling **multi-question interactions** per uploaded document
- Debugging **production issues** (400 / 500 errors, worker timeouts)
- Understanding **infrastructure constraints** of free cloud tiers
- Deciding between **local models vs API-based AI services**

---

## ⚠️ Deployment Notes
- Local embedding models can exceed memory limits on free cloud tiers
- This project helped me understand **real-world GenAI infra trade-offs**
- Designed with safety in mind: no cross-user data leakage

---

## ▶️ Run Locally
```bash
pip install -r requirements.txt
python app.py
````

Then open:

```
http://127.0.0.1:5000
```

---

## 👤 Author

**Hari Ragavendiran R**
Final-year Engineering Student | Python & GenAI Enthusiast

* GitHub: [https://github.com/HariRagavanR](https://github.com/HariRagavanR)
* LinkedIn: [https://www.linkedin.com/in/hari-ragavendiran-r-a61679259](https://www.linkedin.com/in/hari-ragavendiran-r-a61679259)

---

## 📌 Future Improvements

* API-based embeddings for better scalability
* Chat-style conversation UI
* PDF preview alongside answers
* Vector database integration
* Authentication & user history

---

⭐ If you find this project useful, feel free to star the repository!

