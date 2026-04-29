from src.embedder import create_embeddings, model
from src.retriever import Retriever
from src.generator import generate_answer

# Load knowledge
with open("data/knowledge.txt", "r") as f:
    texts = f.read().split("\n\n")

# Create embeddings
embeddings = create_embeddings(texts)

# Create retriever
retriever = Retriever(embeddings, texts)

print("🤖 RAG Chatbot (type 'exit' to quit)")

while True:
    query = input("\nYou: ")

    if query.lower() == "exit":
        break

    query_embedding = model.encode(query)

    results = retriever.search(query_embedding)
    context = results[0]

    answer = generate_answer(context, query)

    print("Bot:", answer)