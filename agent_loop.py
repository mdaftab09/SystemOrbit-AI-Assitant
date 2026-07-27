import ollama

# 1. Define the tool
def create_jira_ticket(issue_description: str) -> str:
    """Creates an IT support Jira ticket for a user."""
    print(f"\n[SYSTEM EXECUTING TOOL] -> Creating ticket for: {issue_description}")
    return "Ticket #IT-9999 created successfully."

# Map tool names to actual callable Python functions
available_tools = {
    'create_jira_ticket': create_jira_ticket
}

def run_agent(user_prompt: str):
    print(f"User: {user_prompt}\n")
    
    # Maintain conversation history
    messages = [{"role": "user", "content": user_prompt}]
    
    # PASS 1: Ask the AI what to do
    response = ollama.chat(
        model="llama3.2:1b",
        messages=messages,
        tools=[create_jira_ticket]
    )
    
    # Append the assistant's initial response to history
    messages.append(response['message'])
    
    # Check if the model wants to call a tool
    tool_calls = response['message'].get('tool_calls')
    
    if tool_calls:
        for call in tool_calls:
            function_name = call['function']['name']
            function_args = call['function']['arguments']
            
            if function_name in available_tools:
                # Execute the actual Python function using extracted arguments
                tool_function = available_tools[function_name]
                tool_result = tool_function(**function_args)
                
                # Append the function result back into the conversation
                messages.append({
                    "role": "tool",
                    "content": str(tool_result),
                    "name": function_name
                })
        
        # PASS 2: Pass the function result back to the AI for a final summary
        final_response = ollama.chat(
            model="llama3.2:1b",
            messages=messages
        )
        print("\nSystemOrbit:")
        print(final_response['message']['content'])
    else:
        # If no tool was needed, print the standard response
        print("\nSystemOrbit:")
        print(response['message']['content'])

if __name__ == "__main__":
    run_agent("My laptop screen is broken. Please open a Jira ticket for me.")