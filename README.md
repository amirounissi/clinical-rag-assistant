# Clinical Reasoning Assistant (RAG-based)

---

## 🔍 Overview

This project is a **Clinical Reasoning Assistant** powered by **Retrieval-Augmented Generation (RAG)** techniques.  
It enables users—medical students, clinicians, or researchers—to upload clinical documents (PDFs, case notes, guidelines) and ask natural language questions.  
The assistant retrieves relevant information and generates accurate, context-aware answers using local Large Language Models (LLMs), without relying on external APIs.

---

## 💻 Demo

> *Coming soon!*  
A simple Streamlit web interface allows document upload, question input, and displays generated clinical answers along with source references.

---

## 🛠️ Tech Stack

- **Language:** Python 3.8+  
- **Large Language Models (LLMs):** Mistral 7B (GGUF), GPT4All, Phi-3  
- **Embeddings:** Instructor-XL, Sentence Transformers  
- **Vector Store:** ChromaDB (local)  
- **RAG Framework:** LangChain / LlamaIndex  
- **Document Parsing:** PyMuPDF, pdfplumber  
- **OCR (optional):** Tesseract OCR  
- **Interface:** Streamlit  
- **Model Runner:** llama.cpp or transformers pipeline  

---

## 📁 Folder Structure
clinical-rag-assistant/
│
├── app/
│ ├── ingest.py # Document ingestion and vectorization
│ ├── retriever.py # Semantic search logic
│ ├── generator.py # LLM-based answer generation
│ └── interface.py # Streamlit UI frontend
│
├── docs/ # Sample clinical PDFs and documents
├── models/ # Local LLM models (GGUF files)
├── vectorstore/ # Embeddings and vector index data
├── requirements.txt # Python dependencies
└── README.md # Project documentation (this file)