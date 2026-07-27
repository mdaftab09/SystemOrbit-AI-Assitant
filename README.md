# 🚀 SystemOrbit

> An autonomous internal support assistant featuring **RAG (Retrieval-Augmented Generation)** and **Agentic tool-calling workflows**, powered by local LLMs.

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100%2B-009688.svg)](https://fastapi.tiangolo.com/)
[![ChromaDB](https://img.shields.io/badge/ChromaDB-Vector%20Store-orange.svg)](https://www.trychroma.com/)
[![Ollama](https://img.shields.io/badge/Ollama-Local%20LLM-black.svg)](https://ollama.com/)

---

# 📖 About the Project

**SystemOrbit** bridges the gap between traditional AI chat wrappers and real-world backend systems.

Instead of simply answering questions, SystemOrbit acts as an autonomous AI agent that:

- 🔍 Searches private company documentation using semantic vector search (RAG)
- 📚 Reduces hallucinations by grounding responses in internal knowledge
- 🤖 Dynamically executes backend actions through tool/function calling
- ⚡ Automates workflows such as IT ticket generation

---

# 🏗️ Tech Stack

| Technology | Purpose |
|------------|---------|
| **Python** | Core programming language |
| **FastAPI** | Asynchronous REST API |
| **Ollama** | Local LLM inference |
| **Llama 3.2:1B** | Language model |
| **ChromaDB** | Vector database for semantic search |
| **Custom Agent Loop** | Tool routing & state management |

---

# ⚙️ Getting Started

## Prerequisites

Before running the project, install:

- Python 3.10+
- Ollama

### Install Ollama

Download it from:

https://ollama.com/

Then pull the required model:

```bash
ollama run llama3.2:1b
```

---

# 📦 Installation

### 1. Clone the repository

```bash
git clone https://github.com/mdaftab09/SystemOrbit-Ai-Assistant.git
cd SystemOrbit-Ai-Assistant
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it:

**Windows (PowerShell)**

```powershell
.\venv\Scripts\Activate.ps1
```

**macOS / Linux**

```bash
source venv/bin/activate
```

---

### 3. Install dependencies

```bash
pip install fastapi uvicorn chromadb ollama pydantic
```

---

### 4. Start the server

```bash
uvicorn server:app --reload
```

The API will be available at:

```
http://127.0.0.1:8000
```

---

# 🧪 Testing the API

Once the server is running:

1. Open:

```
http://127.0.0.1:8000/docs
```

2. Expand the **POST `/chat`** endpoint.

3. Click **Try it out**.

4. Send the following JSON:

```json
{
  "user_message": "My laptop caught on fire. Can you request a new one for me?"
}
```

5. Observe the terminal logs as:

- Company documents are retrieved from ChromaDB
- Relevant policy is injected into the prompt
- The AI decides whether to call a tool
- The tool executes
- The final response is returned

---

# 📊 System Workflow

```text
Retrieve: User prompt is analyzed and matched against company docs stored in ChromaDB using high-dimensional embeddings.

Augment: Relevant policy data is injected into the system prompt.

Generate & Act: Ollama processes the context; if an action is required, a two-pass tool loop executes the target Python function (e.g., creating a Jira ticket) and returns a synthesized summary.
```

---

# ✨ Key Features

- ✅ Retrieval-Augmented Generation (RAG)
- ✅ Local LLM via Ollama
- ✅ ChromaDB semantic vector search
- ✅ FastAPI REST backend
- ✅ Autonomous tool/function calling
- ✅ Two-pass agent execution loop
- ✅ Hallucination reduction through grounded context

---

# 🚀 Future Improvements

- Authentication & user management
- Streaming responses
- Persistent ChromaDB storage
- Multi-tool orchestration
- Docker deployment
- Kubernetes support
- Monitoring & observability

---

# 📄 License

This project is open-source and available under the **MIT License**.
