# 🏥 Medical AI Doctor Chatbot 🤖💊


A Retrieval-Augmented Generation (RAG)-powered AI Doctor chatbot built with LangChain, Google Gemini, Pinecone, Flask, and deployed on AWS EC2 with Docker & GitHub Actions.

---

### 📌 Project Overview

This project is an AI-powered Medical Chatbot that acts like a virtual doctor.
It uses Retrieval-Augmented Generation (RAG) to provide reliable, book-based answers from **The Gale Encyclopedia of Medicine.**

✅ If a user asks a medical-related question, the chatbot retrieves the answer from the encyclopedia.

❌ If the question is out of context, it politely responds:

   **“I am sorry, but this document does not contain the answer to this question. I do not have access to external websites or specific files online.”**

---

### 🚀 Features

* 📖 Domain-specific knowledge from the Gale Encyclopedia of Medicine

* 🔎 RAG pipeline with Pinecone Vector Database

* 🤖 Google Gemini 1.5 Flash (Free model) as LLM

* 🛠 LangChain for orchestration

* 🌐 Flask Web App frontend

* 🐳 Dockerized Application for portability

* ☁️ Deployed on AWS EC2 using Docker + GitHub Actions CI/CD

* ⚡ Out-of-context filtering for irrelevant queries

* ✅ Vector Database with Pinecone – Stores embeddings for efficient retrieval.


---

### 🏗️ System Architecture

**Flow:**

* User enters a medical query in the chatbot UI.

* Flask app forwards query to LangChain pipeline.

* Pinecone retrieves relevant passages from the Gale Encyclopedia.

* Google Gemini LLM generates an answer.

* Response is displayed to the user.

* Frontend with HTML & CSS – Clean, responsive chatbot UI.

---

### 🛠 Tech Stack

* Programming Language: Python

* Frameworks & Libraries: LangChain, Flask

* LLM: Google Gemini 1.5 Flash

* Database: Pinecone Vector DB

* Deployment: AWS EC2, Docker, GitHub Actions

* Version Control: Git & GitHub

### 📂 Project Structure
```
📦 medical-ai-chatbot
├── 📄 app.py               # Flask app
├── 📄 requirements.txt     # Dependencies
├── 📄 Dockerfile           # Docker config
├── 📄 .github/workflows/   # GitHub Actions CI/CD pipeline
├── 📄 README.md            # Documentation
├── 📂 assets/              # Images (architecture, screenshots, etc.)
└── 📂 src/                 # RAG pipeline & utils

```

### ⚙️ Installation & Setup

🔹 **Clone the repository**
```
git clone https://github.com/your-username/medical-ai-chatbot.git
cd medical-ai-chatbot
```

🔹 **Create virtual environment & install dependencies**
```
python -m venv venv
source venv/bin/activate   # for Linux/Mac
venv\Scripts\activate      # for Windows

pip install -r requirements.txt
```

🔹 **Set up environment variables**
Create a .env file with:
```
GOOGLE_API_KEY=your_google_api_key
PINECONE_API_KEY=your_pinecone_api_key
PINECONE_ENV=your_pinecone_env
```

### ☁️ Deployment on AWS EC2

* Pushed Docker image to AWS ECR
* Used GitHub Actions CI/CD for automated deployment
* Flask app runs on EC2 inside Docker container

### 📸 Screenshots


### 📜 License

This project is licensed under the MIT License.

✨ Built with ❤️ by Aman Prajapati
