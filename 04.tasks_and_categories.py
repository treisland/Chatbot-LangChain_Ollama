"""
AI assistant that remembers the history of the chat.
It keeps track of items in a list and can recall them.
"""

import os
from dotenv import load_dotenv
from langchain_community.chat_models import ChatOllama
from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser
from langchain_community.chat_message_histories import ChatMessageHistory

load_dotenv()

llm = ChatOllama(
    model=os.getenv("OLLAMA_DEFAULT_MODEL"),
    base_url=os.getenv("OLLAMA_DEFAULT_SERVER")
)

chat_history = ChatMessageHistory()

prompt = ChatPromptTemplate.from_messages([
    ("system", """
    You are a friendly AI assistant. Your goal is to help to keep track of a task entered by a user
    and categorize it appropriately.
    You should remember all the tasks entered by the user and their category.
    There is a one-to-many relationship between tasks and categories.
    Categories can have many tasks and a task can belong to one category.
    Your response should be in the form of a list of all the categories and their respective tasks as a list.
    Do not remove any previous tasks or categories.
    """),

    MessagesPlaceholder(variable_name="messages"),
    ("human", "My task is to '{task}'")
])

chain = prompt | llm | StrOutputParser()

print("\nAI an assistant. Enter a task and I will remember it. Type 'exit' to quit.")

while True:
    task = input("\n\nTask: ")

    if task.lower() == "exit":
        break

    print("\nAssistant: ", end="")

    full_response = []

    # stream the response from the chain

    for chunk in chain.stream({"task": task, "messages": chat_history.messages}):
        print(chunk, end="", flush=True)
        full_response.append(chunk)

    # update the chat history with the new messages
    chat_history.add_messages([HumanMessage(content=task), AIMessage(content="".join(full_response))])
