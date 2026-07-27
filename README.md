import base64
from weasyprint import HTML

html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>SystemOrbit - Project Documentation & README</title>
    <style>
        @page {
            size: A4;
            margin: 20mm 15mm;
            background-color: #fafbfc;
        }
        body {
            font-family: 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
            color: #24292e;
            line-height: 1.6;
            margin: 0;
            padding: 0;
            font-size: 11pt;
        }
        *, *::before, *::after {
            box-sizing: border-box;
        }
        h1 {
            color: #0366d6;
            font-size: 24pt;
            text-align: center;
            margin-bottom: 5px;
            text-transform: uppercase;
            letter-spacing: 1px;
        }
        .subtitle {
            text-align: center;
            color: #586069;
            font-size: 12pt;
            margin-bottom: 30px;
            font-style: italic;
        }
        h2 {
            color: #24292e;
            font-size: 16pt;
            border-bottom: 2px solid #e1e4e8;
            padding-bottom: 8px;
            margin-top: 30px;
            margin-bottom: 15px;
            page-break-after: avoid;
        }
        h3 {
            color: #0366d6;
            font-size: 13pt;
            margin-top: 20px;
            margin-bottom: 10px;
            page-break-after: avoid;
        }
        .section-box {
            background: #ffffff;
            border: 1px solid #e1e4e8;
            border-radius: 6px;
            padding: 20px;
            margin-bottom: 25px;
        }
        ul {
            margin-top: 0;
            padding-left: 20px;
        }
        li {
            margin-bottom: 6px;
        }
        code {
            font-family: Consolas, Monaco, monospace;
            background-color: #f6f8fa;
            padding: 2px 4px;
            border-radius: 4px;
            font-size: 10pt;
            color: #d73a49;
        }
        pre {
            background-color: #f6f8fa;
            border: 1px solid #e1e4e8;
            border-radius: 6px;
            padding: 12px;
            font-family: Consolas, Monaco, monospace;
            font-size: 9.5pt;
            overflow-x: auto;
            line-height: 1.4;
        }
        .badge {
            display: inline-block;
            background-color: #0366d6;
            color: white;
            padding: 3px 8px;
            border-radius: 4px;
            font-size: 9pt;
            font-weight: bold;
            margin-right: 5px;
        }
    </style>
</head>
<body>

    <h1>SystemOrbit 🚀</h1>
    <div class="subtitle">Autonomous Internal Support Assistant with RAG & Agentic Workflows</div>

    <div class="section-box">
        <h2>About The Project</h2>
        <p><strong>SystemOrbit</strong> bridges the gap between traditional AI chat wrappers and real-world backend systems. Instead of merely answering questions, SystemOrbit acts as an autonomous agent: it searches private company documentation using semantic vector math to prevent hallucinations, and dynamically executes real actions (such as automated IT ticket generation) via tool/function calling.</p>
        
        <h3>Core Architecture & Tech Stack</h3>
        <ul>
            <li><strong>Language:</strong> Python</li>
            <li><strong>Web Framework:</strong> FastAPI (Asynchronous REST API)</li>
            <li><strong>LLM Engine:</strong> Ollama (<code>llama3.2:1b</code> running locally)</li>
            <li><strong>Vector Store:</strong> ChromaDB (In-memory semantic search via embeddings)</li>
            <li><strong>Agentic Loop:</strong> Custom two-pass execution engine handling dynamic tool routing and state management.</li>
        </ul>
    </div>

    <div class="section-box">
        <h2>Getting Started Locally</h2>
        <p>Follow these steps to set up and run SystemOrbit on your local machine.</p>
        
        <h3>Prerequisites</h3>
        <p>Make sure you have Python and Ollama installed on your system. Pull the required model via your terminal:</p>
        <pre>ollama run llama3.2:1b</pre>

        <h3>Installation Steps</h3>
        <ol>
            <li><strong>Clone the repository:</strong><br><code>git clone https://github.com/mdaftab09/SystemOrbit.git</code><br><code>cd SystemOrbit</code></li>
            <li><strong>Create and activate a virtual environment:</strong><br><code>python -m venv venv</code><br><code>.\\venv\\Scripts\\Activate.ps1</code></li>
            <li><strong>Install dependencies:</strong><br><code>pip install fastapi uvicorn chromadb ollama pydantic</code></li>
            <li><strong>Run the server:</strong><br><code>uvicorn server:app --reload</code></li>
        </ol>
    </div>

    <div class="section-box">
        <h2>Testing the API</h2>
        <p>Once the server is running, you can interact with it using FastAPI's built-in interactive documentation:</p>
        <ul>
            <li>Open your browser and navigate to: <code>http://127.0.0.1:8000/docs</code></li>
            <li>Expand the <code>POST /chat</code> endpoint and click <strong>"Try it out"</strong>.</li>
            <li>Send a JSON payload:</li>
        </ul>
        <pre>{
  "user_message": "My laptop caught on fire. Can you request a new one for me?"
}</pre>
    </div>

    <div class="section-box">
        <h2>System Workflow</h2>
        <ul>
            <li><strong>1. Retrieve:</strong> User prompt is analyzed and matched against company docs stored in ChromaDB using high-dimensional embeddings.</li>
            <li><strong>2. Augment:</strong> Relevant policy data is injected into the system prompt.</li>
            <li><strong>3. Generate & Act:</strong> Ollama processes the context; if an action is required, a two-pass tool loop executes the target Python function (e.g., creating a Jira ticket) and returns a synthesized summary.</li>
        </ul>
    </div>

</body>
</html>
"""
