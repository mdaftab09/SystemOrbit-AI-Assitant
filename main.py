import ollama

def ask_system_orbit(user_question):
    # Step 1: Build the array of dictionaries
    conversation = [
        {"role": "system", "content": "You are SystemOrbit, a helpful and brief AI assistant. Always answer in one short sentence."},
        {"role": "user", "content": user_question}
    ]
    
    # Step 2: Pass the array to our local engine
    # Specied the exact model we downloaded earlier
    response = ollama.chat(model="llama3.2:1b", messages=conversation)
    
    # Step 3: Extracting the answer
    # Ollama returns a large dictionary full of metadata (like how long it took to process).
    # We navigate through the keys to grab just the text content of the AI's reply.
    return response['message']['content']

# Step 4: Test the function
if __name__ == "__main__":
    print("Waking up SystemOrbit...")
    answer = ask_system_orbit("Why is the sky blue?")
    print("\nSystemOrbit says:")
    print(answer)