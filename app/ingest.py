# app/ingest.py

import os 
import pdfplumber
from langchain.text_splitter import RecursiveCharacterTextSplitter
from sentence_transformers import SentenceTransformer
import chromadb
from chromadb.config import Settings

# Initialize embeddings model
embedder = SentenceTransformer('all-MiniLM-L6-v2')

# Initialize ChromaDB client
client = chromadb.Client(Settings(
    chroma_db_impl="duckdb+parquet",
    persist_directory="chroma_db"
))
collection = client.get_or_create_collection(name="documents")


def load_pdf(file_path):
    """Load PDF file and extract text."""
    with pdfplumber.open(file_path) as pdf:
        text = ""
        for page in pdf.pages:
            text += page.extract_text() + "\n"
    return text

def chunk_text(text,chunk_size=500,chunk_overlap=50):
    """Split text into manageable chunks."""
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap
    )
    return text_splitter.split_text(text)

def ingest_docs(doc_folder="docs"):
    for filename in os.listdir(doc_folder):
        if filename.endswith('.pdf'):
            file_path = os.path.join(doc_folder, filename)
            print(f"Ingesting {file_path}...")
            text = load_pdf(file_path)
            chunks = chunk_text(text)
            #create embeddings for each chunk   
            embeddings = embedder.encode(chunks, show_progress_bar=True)
            #upsert into ChromaDB
            ids = [f"{filename}_{i}" for i in range(len(chunks))]
            metadatas = [{"source": filename} for _ in chunks]
            collection.upsert(
                documents=chunks,
                embeddings=embeddings,
                metadatas=metadatas,
                ids=ids
            )
    #presist to disk 
    client.persist()
    print("Ingestion complete.")
if __name__ == "__main__":
    ingest_docs()
