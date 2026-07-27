import chromadb

# Step 1: Initialize the Vector Database (running locally)
client = chromadb.Client()

# Step 2: Create a "Collection" to hold our documents
collection = client.create_collection(name="company_docs")

print("Adding documents to the Vector Database...")

# Step 3: Add documents. 
collection.add(
    documents=[
        "The guest wifi password is 'OrbitGuest2026!'.",
        "Employees receive 20 days of paid time off per year.",
        "To request a new laptop, you must submit a Jira ticket to the IT department."
    ],
    ids=["doc1", "doc2", "doc3"] # Every document needs a unique ID
)

# Step 4: Perform a Semantic Search
user_query = "How much vacation do I get?"
print(f"\nUser asked: '{user_query}'")
print("Searching for the closest meaning in the database...")

# We ask the database for the top 1 most mathematically similar document
results = collection.query(
    query_texts=[user_query],
    n_results=1 
)

print("\nDatabase found this document:")
print(results['documents'])