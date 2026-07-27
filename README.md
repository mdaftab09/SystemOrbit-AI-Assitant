# SystemOrbit 🚀

> An autonomous internal support assistant featuring RAG (Retrieval-Augmented Generation) and Agentic tool-calling workflows, powered by local LLMs.

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100%2B-009688.svg)](https://fastapi.tiangolo.com/)
[![ChromaDB](https://img.shields.io/badge/ChromaDB-Vector%20Store-orange.svg)](https://www.trychroma.com/)
[![Ollama](https://img.shields.io/badge/Ollama-Local%20LLM-black.svg)](https://ollama.com/)

---

## 📖 About The Project

**SystemOrbit** bridges the gap between traditional AI chat wrappers and real-world backend systems. Instead of merely answering questions, SystemOrbit acts as an autonomous agent: it searches private company documentation using semantic vector math to prevent hallucinations and dynamically executes real actions (such as automated IT ticket generation) via tool/function calling.

### 🏗️ Core Architecture & Tech Stack
* **Language:** Python
* **Web Framework:** FastAPI (Asynchronous REST API)
* **LLM Engine:** Ollama (`llama3.2:1b` running locally)
* **Vector Store:** ChromaDB (In-memory semantic search via embeddings)
* **Agentic Loop:** Custom two-pass execution engine handling dynamic tool routing and state management.

---

## ⚙️ Getting Started Locally

Follow these steps to set up and run SystemOrbit on your local machine.

### Prerequisites
Make sure you have **Python** and **Ollama** installed on your system.
1. Download and install [Ollama](https://ollama.com/).
2. Pull the required local model via your terminal:
   ```bash
   ollama run llama3.2:1b
   ```
   ---
## Installation & Setup
1.Clone the repository:
git clone [https://github.com/mdaftab09/SystemOrbit-Ai-Assistant.git](https://github.com/mdaftab09/SystemOrbit-Ai-Assistant.git)
cd SystemOrbit

2.Create and activate a virtual environment:
```bash
python -m venv venv
# On Windows:
.\venv\Scripts\Activate.ps1
# On macOS/Linux:
# source venv/bin/activate
```
3.Install dependencies:
```bash
pip install fastapi uvicorn chromadb ollama pydantic
```
4.Run the server:
```bash
uvicorn server:app --reload
```
---
##🧪 Testing the API
Once the server is running, you can interact with it using FastAPI's built-in interactive documentation:

1.Open your browser and navigate to: http://127.0.0.1:8000/docs

2.Expand the POST /chat endpoint.

3.Click "Try it out" and send a JSON payload:
```
{
  "user_message": "My laptop caught on fire. Can you request a new one for me?"
}
```
4.Observe the terminal logs as the RAG pipeline retrieves the company policy, the agent autonomously triggers the tool execution loop, and the server returns the final response.
---
##📊 System Workflow
Retrieve: User prompt is analyzed and matched against company docs stored in ChromaDB using high-dimensional embeddings.

Augment: Relevant policy data is injected into the system prompt.

Generate & Act: Ollama processes the context; if an action is required, a two-pass tool loop executes the target Python function (e.g., creating a Jira ticket) and returns a synthesized summary.
