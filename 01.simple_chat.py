"""
This a simple chat loop with no history
"""

import os
from dotenv import load_dotenv
from langchain_community.chat_models import ChatOllama

load_dotenv()

llm = ChatOllama(
    base_url=os.getenv("OLLAMA_HOST"),
    model=os.getenv("OLLAMA_MODEL")
)

while True:

    prompt = input("\n\nUser: ")

    if prompt == "exit":
        break

    response = llm.invoke(prompt)

    print(f"\nAssistant: {response.content}", end="", flush=True)


