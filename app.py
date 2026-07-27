import chromadb
import ollama

def setup_database():
    """Initializes the database and loads our dummy documents."""
    # In-memory client is being usrd. 
    # Every time the script runs, it starts fresh.
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
    return collection

def ask_system_orbit(collection, user_query):
    """The RAG Pipeline: Retrieve -> Augment -> Generate"""
    
    # Step 1: RETRIEVE the most relevant document
    print("Searching company records...")
    db_results = collection.query(
        query_texts=[user_query],
        n_results=1
    )
    
    # Extract the plain text string of the document we found
    found_document = db_results['documents'][0][0]
    print(f"(Found context: {found_document})")
    
    # Step 2: AUGMENT the context into the system prompt
    # Telling the AI explicitly tO ONLY use the provided context.
    system_instruction = f"""
    You are SystemOrbit, an internal IT assistant. 
    Answer the user's question using ONLY the following company document:
    {found_document}
    
    If the document does not contain the answer, say "I don't know."
    Keep your answer brief and conversational.
    """
    
    conversation = [
        {"role": "system", "content": system_instruction},
        {"role": "user", "content": user_query}
    ]
    
    # Step 3: GENERATE the response
    print("Thinking...")
    ai_response = ollama.chat(model="llama3.2:1b", messages=conversation)
    
    return ai_response['message']['content']

# --- Main Execution ---
if __name__ == "__main__":
    # Setup
    my_db = setup_database()
    
    # Test our pipeline
    question = "Hey! I need to know how much vacation time I am allowed to take this year."
    print(f"\nUser: {question}\n")
    
    answer = ask_system_orbit(my_db, question)
    
    print("\nSystemOrbit:")
    print(answer)