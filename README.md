# 📄 DocuMind AI
### Intelligent PDF Question Answering System using RAG (Retrieval-Augmented Generation)

![Python](https://img.shields.io/badge/Python-3.13-blue?logo=python)
![Flask](https://img.shields.io/badge/Flask-Web%20Framework-black?logo=flask)
![Gemini](https://img.shields.io/badge/Google-Gemini%20API-blue?logo=google)
![FAISS](https://img.shields.io/badge/FAISS-Vector%20Database-green)
![License](https://img.shields.io/badge/License-MIT-orange)

---

## 📌 Overview

DocuMind AI is an intelligent document question-answering system built using the **Retrieval-Augmented Generation (RAG)** architecture.

Instead of asking a Large Language Model (LLM) to answer questions from its own knowledge, the application first retrieves the most relevant information from an uploaded PDF and then uses Google's Gemini API to generate accurate answers grounded in the document.

This significantly reduces hallucinations and allows users to interact naturally with documents such as:

- Resume PDFs
- Research Papers
- Reports
- Books
- Study Material
- Documentation
- Company Policies
- Technical Manuals

---

# 🚀 Live Demo

**Live Website**

https://documind-ai-ii0p.onrender.com/

---



# ✨ Features

✅ Upload any PDF document

✅ Automatic PDF text extraction

✅ Intelligent text chunking

✅ Embedding generation using Gemini

✅ FAISS vector database

✅ Semantic similarity search

✅ Retrieval-Augmented Generation (RAG)

✅ Natural language question answering

✅ Modern responsive UI

✅ Flask REST API

✅ Real-time chat interface

---

# 🏗️ System Architecture

```
                User
                  │
                  ▼
          Upload PDF File
                  │
                  ▼
          PDF Text Extraction
          (PyMuPDF / fitz)
                  │
                  ▼
            Text Chunking
                  │
                  ▼
      Gemini Embedding Model
                  │
                  ▼
        FAISS Vector Database
                  │
                  ▼
          User Question
                  │
                  ▼
      Question Embedding
                  │
                  ▼
      Similarity Search (FAISS)
                  │
                  ▼
      Relevant Context Chunks
                  │
                  ▼
        Prompt Construction
                  │
                  ▼
         Gemini Flash Model
                  │
                  ▼
           Final Response
```

---

# 🧠 RAG Pipeline

The project follows the Retrieval-Augmented Generation workflow.

## Step 1

Upload PDF

↓

## Step 2

Extract Text

↓

## Step 3

Chunk Document

↓

## Step 4

Generate Embeddings

↓

## Step 5

Store Embeddings inside FAISS

↓

## Step 6

User asks question

↓

## Step 7

Generate Question Embedding

↓

## Step 8

Retrieve Top Matching Chunks

↓

## Step 9

Build Prompt

↓

## Step 10

Gemini generates answer only using retrieved context

---

# 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| Python | Programming Language |
| Flask | Backend Framework |
| HTML5 | Frontend |
| CSS3 | Styling |
| JavaScript | Client-side Logic |
| Google Gemini API | LLM & Embeddings |
| FAISS | Vector Database |
| PyMuPDF | PDF Processing |
| NumPy | Numerical Operations |
| dotenv | Environment Variables |

---

# 📂 Project Structure

```
DocuMind-AI/

│

├── app.py

├── config.py

├── requirements.txt

├── .env

│

├── rag/

│   ├── pdf_loader.py

│   ├── chunker.py

│   ├── embeddings.py

│   ├── vector_store.py

│   ├── retriever.py

│   ├── prompt_builder.py

│   ├── gemini_client.py

│   ├── rag_pipeline.py

│   └── document_processor.py

│

├── static/

│   ├── css/

│   │      style.css

│   │

│   └── js/

│          script.js

│

├── templates/

│      index.html

│

├── uploads/

│

└── vector_db/

       faiss.index

       chunks.pkl
```

---

# ⚙️ Installation

## Clone Repository

```bash
git clone https://github.com/Maanasb26/DocuMind-AI.git

cd DocuMind-AI
```

---

## Create Virtual Environment

Windows

```bash
python -m venv venv

venv\Scripts\activate
```

macOS/Linux

```bash
python3 -m venv venv

source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Create Environment File

Create a file named

```
.env
```

Add your Gemini API key

```env
GEMINI_API_KEY=YOUR_API_KEY_HERE
```

---

## Run Application

```bash
python app.py
```

Open

```
http://127.0.0.1:5000
```

---

# 🔄 Workflow

### Upload PDF

↓

Text Extraction

↓

Chunk Generation

↓

Embedding Generation

↓

Store into FAISS

↓

Ask Question

↓

Retrieve Relevant Chunks

↓

Generate Final Answer

---

# 📡 API Endpoints

## Home

```
GET /
```

Returns the application interface.

---

## Upload PDF

```
POST /upload
```

Uploads and indexes the document.

---

## Ask Question

```
POST /ask
```

Example Request

```json
{
  "question":"What is the candidate's CGPA?"
}
```

Example Response

```json
{
   "answer":"The candidate's CGPA is 8.50."
}
```

---

# 🧪 Example

### Upload

```
Resume.pdf
```

Question

```
What is the candidate's CGPA?
```

Answer

```
The candidate's CGPA is 8.50.
```

---

# 🔍 How Retrieval Works

1. User uploads PDF

2. PDF is converted into plain text

3. Text is split into manageable chunks

4. Each chunk is converted into a vector embedding

5. Embeddings are stored inside FAISS

6. User asks a question

7. Question is converted into an embedding

8. FAISS retrieves the nearest chunks

9. Retrieved context is inserted into the prompt

10. Gemini generates an answer using only the retrieved information

---

# 📈 Future Improvements

- Multiple PDF support
- Chat history
- Conversation memory
- Streaming responses
- OCR support for scanned PDFs
- Citation with page numbers
- Source highlighting
- Authentication
- User accounts
- Cloud vector databases
- Docker deployment
- Kubernetes deployment
- Redis caching
- LangChain integration
- LlamaIndex integration

---

# 🎯 Learning Outcomes

This project demonstrates practical understanding of:

- Retrieval-Augmented Generation (RAG)
- Vector Databases
- Embedding Models
- Semantic Search
- Prompt Engineering
- REST APIs
- Flask Development
- PDF Processing
- LLM Integration
- AI Application Deployment

---

# 🤝 Contributing

Contributions are welcome.

1. Fork the repository

2. Create a feature branch

```bash
git checkout -b feature-name
```

3. Commit changes

```bash
git commit -m "Add new feature"
```

4. Push

```bash
git push origin feature-name
```

5. Create a Pull Request

---

# 📜 License

This project is licensed under the MIT License.

---

# 👨‍💻 Author

**Maanas Brahme**

B.Tech Computer Science Engineering

Vellore Institute of Technology

GitHub

https://github.com/Maanasb26

---

# ⭐ Support

If you found this project helpful, please consider giving it a ⭐ on GitHub.

It helps others discover the project and motivates future development.

---

## Thank You!

Thank you for visiting the repository.

Happy Coding! 🚀
