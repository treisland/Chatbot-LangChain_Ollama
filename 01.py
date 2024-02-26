import os

#chat loop with history

from dotenv import load_dotenv
from langchain_community.chat_models import ChatOllama

load_dotenv()

llm = ChatOllama(
    base_url=os.getenv("OLLAMA_DEFAULT_SERVER"),
    model=os.getenv("OLLAMA_DEFAULT_MODEL")
)

while True:

    prompt = input("\nUser: ")

    if prompt == "exit":
        break

    response = llm.invoke(prompt)

    print(f"\nAssistant: {response.content}", end="", flush=True)

    import os

    from dotenv import load_dotenv
    from langchain_community.chat_models import ChatOllama

    load_dotenv()

    llm = ChatOllama(
        base_url=os.getenv("OLLAMA_DEFAULT_SERVER"),
        model=os.getenv("OLLAMA_DEFAULT_MODEL")
    )

    while True:
        prompt = input("\n\nUser: ")

        if prompt.lower() == "exit":
            break

        response = llm.invoke(prompt)

        print(f"\nAssistant: {response.content}", end="", flush=True)

