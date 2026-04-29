 🤖 Smart FAQ Chatbot (RAG-Based System)

This project is developed as part of the Calder AI/ML Internship selection process.

 🚀 Project Overview
The Smart FAQ Chatbot is an advanced question-answering system built using **Retrieval-Augmented Generation (RAG)** techniques. 

Instead of relying on predefined responses, the system retrieves relevant context from a knowledge base using embeddings and vector similarity search, and generates answers based on that retrieved information.

 🎯 Objective
- Convert a knowledge base into embeddings
- Store embeddings using a vector database (FAISS)
- Retrieve context based on user queries
- Generate accurate responses using retrieved content

 🧠 System Architecture (RAG Pipeline)
User Query
↓
Text Embedding (Sentence Transformer)
↓
Vector Search (FAISS)
↓
Retrieve Relevant Context
↓
Response Generation


✨ Features
- 🧠 Embedding-based semantic search
- 🔍 Fast vector similarity search using FAISS
- 📄 Knowledge base support (text file)
- ⚡ Context-aware responses
- 🧩 Modular and scalable architecture

 🛠️ Technologies Used
- Python
- Sentence Transformers (for embeddings)
- FAISS (Facebook AI Similarity Search)
- NumPy

 📂 Project Structure
 rag_chatbot/
│── data/
│ └── knowledge.txt
│── src/
│ ├── embedder.py
│ ├── retriever.py
│ └── generator.py
│── app.py
│── requirements.txt
│── README.md
