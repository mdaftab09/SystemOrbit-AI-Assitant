import ollama

# Step 1: Define our Tool (The "Hands")
# Notice the type hint (str) and the description. The AI reads these!
def create_jira_ticket(issue_description: str) -> str:
    """Creates an IT support Jira ticket for a user."""
    
    # In a production app, we would put real API connection code here.
    # For now, we are just mocking the action.
    print(f"\n[SYSTEM ACTION FIRED] -> Creating ticket for: {issue_description}")
    return "Ticket #IT-9999 created successfully."

# Step 2: The User Request
user_prompt = "My laptop screen keeps flickering and turning green. Can you create a Jira ticket for me?"
print(f"User asked: '{user_prompt}'")
print("Thinking...\n")

# Step 3: Call the AI and pass in our tools
response = ollama.chat(
    model="llama3.2:1b",
    messages=[{"role": "user", "content": user_prompt}],
    tools=[create_jira_ticket] # We pass the actual Python function in a list!
)

# Step 4: Check the AI's decision
# check if the AI decided it needed to use a tool, or if it just replied with text.
if response['message'].get('tool_calls'):
    print("SUCCESS! The AI decided it needs to use a tool:")
    # Print out the raw data the AI sent back asking us to run the function
    for tool in response['message']['tool_calls']:
        print(f"Tool Name: {tool['function']['name']}")
        print(f"Arguments: {tool['function']['arguments']}")
else:
    print("The AI didn't use the tool. It just replied:")
    print(response['message']['content'])