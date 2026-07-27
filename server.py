from fastapi import FastAPI
from pydantic import BaseModel
import ollama
import chromadb

# --- 1. SETUP THE WAITER (FastAPI) ---
app = FastAPI(title="SystemOrbit AI API")

class ChatRequest(BaseModel):
    user_message: str

# --- 2. SETUP THE MEMORY (ChromaDB) ---
print("Booting up Vector Database...")
client = chromadb.Client()
collection = client.create_collection(name="system_orbit_docs")
collection.add(
    documents=[
        "The guest wifi password is 'OrbitGuest2026!'.",
        "Employees receive 20 days of paid time off per year.",
        "To request a new laptop, you must submit a Jira ticket to the IT department."
    ],
    ids=["doc1", "doc2", "doc3"]
)

# --- 3. SETUP THE HANDS (Tools) ---
def create_jira_ticket(issue_description: str) -> str:
    """Creates an IT support Jira ticket for a user."""
    print(f"\n[SYSTEM EXECUTING TOOL] -> Creating ticket for: {issue_description}")
    return "Ticket #IT-9999 created successfully."

available_tools = {'create_jira_ticket': create_jira_ticket}


# --- 4. THE MAIN ENGINE (The API Route) ---
@app.post("/chat")
def chat_endpoint(request: ChatRequest):
    user_prompt = request.user_message
    print(f"\n--- New Request: {user_prompt} ---")

    # Step A: Retrieve Memory (RAG)
    db_results = collection.query(query_texts=[user_prompt], n_results=1)
    found_document = db_results['documents'][0][0]
    print(f"Memory Retrieved: {found_document}")

    # Step B: Build the AI Prompt
    system_prompt = f"""
    You are SystemOrbit, an internal IT assistant. 
    Use this company document to answer the user: {found_document}
    If the document says to submit a Jira ticket, use your tool to do it!
    """
    
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt}
    ]

    # Step C: Ask the AI (Pass 1)
    response = ollama.chat(
        model="llama3.2:1b",
        messages=messages,
        tools=[create_jira_ticket]
    )
    messages.append(response['message'])

    # Step D: Check if the AI wants to use a Tool
    tool_calls = response['message'].get('tool_calls')
    
    if tool_calls:
        print("AI is using a tool!")
        for call in tool_calls:
            func_name = call['function']['name']
            func_args = call['function']['arguments']
            
            if func_name in available_tools:
                # Execute the tool
                result = available_tools[func_name](**func_args)
                
                # Add the result back to the conversation
                messages.append({
                    "role": "tool", 
                    "content": str(result), 
                    "name": func_name
                })

        # Ask the AI to summarize the tool result (Pass 2)
        final_response = ollama.chat(model="llama3.2:1b", messages=messages)
        return {"reply": final_response['message']['content']}

    # Step E: If no tool was needed, just return the text
    return {"reply": response['message']['content']}