"""
A simple python assistant that answers questions about python programming.
It uses prompt templates to generate the prompts and the output parser to make the AI response more readable.
"""

import os
from dotenv import load_dotenv
from langchain_community.chat_models import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Load the environment variables
load_dotenv()

# Create a ChatOllama instance

llm = ChatOllama(
    base_url=os.getenv("OLLAMA_HOST"),
    model=os.getenv("OLLAMA_MODEL")
)

chat_history = []

prompt = ChatPromptTemplate.from_messages([
    ("system",
     """You are python developer who enjoys answering questions about programming.
     Your answers are concise and to the point. You will answer questions about python programming),
     """),
    ("human", "What can you tell me about {topic}?")
])

chain = prompt | llm | StrOutputParser()

print("\nAI an assistant. Enter a question about python programming and I will answer it. Type 'exit' to quit.")

while True:
    topic = input("\n\nTopic: ")

    if topic.lower() == "exit":
        break

    print("\nAssistant: ", end="")

    for chunk in chain.stream({"topic": topic}):
        print(chunk, end="", flush=True)
