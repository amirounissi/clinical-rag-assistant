# 🧠 Clinical Reasoning Assistant (RAG-based)

A smart assistant that helps medical students, clinicians, and researchers answer clinical questions by searching and understanding medical documents. Built using Retrieval-Augmented Generation (RAG) with open-source LLMs and vector search.

---

## 📌 Features

- 🔍 **Question Answering**: Ask clinical questions and get accurate, contextual answers
- 📄 **Document Upload**: Add your own medical textbooks, articles, or case notes
- 🧠 **RAG Workflow**: Combines semantic search + generation using a local LLM
- 🧾 **Show Sources**: See which document passages were used to generate each answer
- 🖼️ **Optional OCR**: Handle scanned or image-based documents (Tesseract OCR)

---

## 🚀 Technologies Used

| Component            | Tool / Library                         |
|----------------------|----------------------------------------|
| Language             | Python                                 |
| LLM                  | Mistral 7B, Phi-3, GPT4All (offline)   |
| Embeddings           | Sentence Transformers, Instructor-XL   |
| Vector Store         | ChromaDB / FAISS                       |
| RAG Framework        | LangChain / LlamaIndex                 |
| UI                   | Streamlit                              |
| PDF Parsing          | PyMuPDF, pdfplumber                    |
| OCR (optional)       | Tesseract OCR + pytesseract            |

---

## 📁 Project Structure

clinical-rag-assistant/
│
├── app/
│ ├── ingest.py # Load + chunk medical documents
│ ├── retriever.py # Search relevant chunks
│ ├── generator.py # Generate responses using LLM
│ └── interface.py # Streamlit UI
│
├── docs/ # Upload your medical content here
├── models/ # LLM files (GGUF format if local)
├── vectorstore/ # Vector database
├── requirements.txt # Python dependencies
└── README.md # Project description 