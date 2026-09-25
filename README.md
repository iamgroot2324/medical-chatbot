# 🩺 MediBot AI — Medical Chatbot using RAG, FAISS & Groq LLM

<div align="center">

![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge\&logo=python\&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-App-FF4B4B?style=for-the-badge\&logo=streamlit\&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-RAG-green?style=for-the-badge)
![FAISS](https://img.shields.io/badge/FAISS-VectorDB-00599C?style=for-the-badge)
![Groq](https://img.shields.io/badge/Groq-LLM-F55036?style=for-the-badge)
![HuggingFace](https://img.shields.io/badge/HuggingFace-Embeddings-yellow?style=for-the-badge\&logo=huggingface)
![License](https://img.shields.io/badge/License-MIT-blue?style=for-the-badge)

### AI-powered Medical Question Answering Chatbot with Retrieval-Augmented Generation (RAG)

*Built with Streamlit, LangChain, FAISS, Hugging Face Embeddings, and Groq LLM.*

</div>

---

## 📌 Project Overview

**MediBot AI** is an intelligent medical chatbot that answers healthcare-related questions using a **Retrieval-Augmented Generation (RAG)** pipeline.

Instead of relying only on a language model, MediBot searches a medical knowledge base stored in a **FAISS vector database**, retrieves the most relevant medical documents, and generates context-aware responses using a **Groq-hosted LLM**.

This approach helps produce grounded answers based on the provided medical context.

---

## ✨ Features

* 💬 Interactive AI medical chatbot.
* 🧠 Retrieval-Augmented Generation (RAG).
* 📚 FAISS vector database for semantic search.
* 🤗 Hugging Face sentence-transformer embeddings.
* ⚡ Groq LLM for fast inference.
* 📖 Source document viewer.
* 🎨 Modern Streamlit UI/UX.
* 🔒 Environment variables using `.env`.
* 🗑️ Clear chat history option.

---

## 🖥️ Demo UI

### Home Screen

> Replace this image with your own screenshot after running the project.

![Home UI](assets/home.png)

### Chat Example

![Chat Example](assets/chat.png)

### Source Documents

![Source Documents](assets/source.png)

---

## 🏗️ Project Architecture

![Architecture](assets/architecture.png)

### Workflow

1. User asks a medical question.
2. Question is converted into embeddings.
3. FAISS retrieves the top relevant medical documents.
4. Retrieved context is sent to Groq LLM.
5. LLM generates an answer using only the retrieved context.
6. Source documents are displayed to the user.

---

## ⚙️ Tech Stack

| Technology              | Purpose                        |
| ----------------------- | ------------------------------ |
| Python                  | Backend development            |
| Streamlit               | Web interface                  |
| LangChain               | RAG pipeline                   |
| FAISS                   | Vector database                |
| Hugging Face Embeddings | Semantic document embeddings   |
| Groq API                | Large Language Model inference |
| dotenv                  | Secure API key management      |

---

## 📂 Project Structure

```text
medical-chatbot/
│
├── medibot.py                 # Streamlit application
├── requirements.txt            # Python dependencies
├── .env                       # API key (not uploaded)
├── .gitignore
│
├── vectorstore/
│   └── db_faiss/              # FAISS vector database
│
├── data/                      # Medical documents
│
├── assets/                    # Screenshots & architecture images
│   ├── home.png
│   ├── chat.png
│   ├── source.png
│   └── architecture.png
│
└── README.md
```

---

## 🚀 Installation

### 1. Clone the repository

```bash
git clone https://github.com/iamgroot2324/medical-chatbot.git

cd medical-chatbot
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### Windows

```powershell
.venv\Scripts\activate
```

### Linux / macOS

```bash
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Add your Groq API Key

Create a `.env` file.

```env
GROQ_API_KEY=your_groq_api_key_here
```

### 5. Run the application

```bash
streamlit run medibot.py
```

The app will open in your browser at:

```text
http://localhost:8501
```

---

## 💬 Example Questions

You can ask questions like:

* What is diabetes?
* What are the symptoms of asthma?
* What causes hypertension?
* How is pneumonia treated?
* What are the risk factors of heart disease?

---

## 🧠 Retrieval-Augmented Generation Pipeline

### Document Embeddings

Medical documents are converted into embeddings using:

```python
sentence-transformers/all-MiniLM-L6-v2
```

### Vector Search

* Semantic similarity search.
* Top **3** relevant chunks retrieved.
* FAISS performs nearest-neighbor search.

### Language Model

Groq-hosted model:

```text
openai/gpt-oss-120b
```

The LLM generates responses only from retrieved context.

---

## 📸 Screenshots

### Landing Page

![Landing Page](assets/home.png)

### Medical Chat

![Medical Chat](assets/chat.png)

### Retrieved Sources

![Sources](assets/source.png)

---

## 📊 Future Improvements

* Voice input using Speech-to-Text.
* Voice response using Text-to-Speech.
* Chat history stored in a database.
* Multiple medical knowledge bases.
* Authentication and user profiles.
* PDF medical report question answering.
* Multi-language support (English & Nepali).

---

## 🔐 Environment Variables

Create a `.env` file.

```env
GROQ_API_KEY=your_api_key
```

**Never upload `.env` to GitHub.**

---

## 👨‍💻 Author

**Sugam Khatiwada**

BSc CSIT Student • AI & Machine Learning Enthusiast

📍 Kathmandu, Nepal

* GitHub: https://github.com/iamgroot2324
* LinkedIn: https://linkedin.com/in/sugam-khatiwada-804a62343
* Email: [sugamm335@gmail.com](mailto:sugamm335@gmail.com)

---

## ⭐ Support

If you found this project useful, consider giving it a **Star ⭐** on GitHub.
