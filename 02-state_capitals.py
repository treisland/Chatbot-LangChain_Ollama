import os

'''
Chat template for state capitals that streams back the response
'''

from dotenv import load_dotenv
from langchain_community.chat_models import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

llm = ChatOllama(
    base_url=os.getenv("OLLAMA_DEFAULT_SERVER"),
    model=os.getenv("OLLAMA_DEFAULT_MODEL")
)

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a friendly AI assistant. You will answer questions about state capitals."),
    ("human", "What is the capital of Georgia?"),
    ("assistant", "The capital of Georgia is Atlanta. Would you like to know the capital of another state?"),
    ("human", "{state}"),
])

chain = prompt | llm | StrOutputParser()

print("\nAI an assistant. Enter the name of a state and I will answer with it's capital. Type 'exit' to quit.")

while True:
    state_name = input("\n\nState: ")

    if state_name.lower() == "exit":
        break

    print(f"\nAssistant: ", end="")

    for chunk in chain.stream({"state": state_name}):
        print(chunk, end="", flush=True)
