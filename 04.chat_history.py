"""
This example demonstrates how to use the ChatMessageHistory class
to store the chat messages and use them as input to the AI model.
"""

import os
from dotenv import load_dotenv
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_community.chat_models import ChatOllama
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser

# Load environment variables
load_dotenv()

# initialize the LLM and set the model

llm = ChatOllama(
    base_url=os.getenv("OLLAMA_HOST"),
    model=os.getenv("OLLAMA_MODEL")
)

# create a prompt template
prompt = ChatPromptTemplate.from_messages([
    ("system", """
    You are a friendly research assistant.  
    You will provide thoughtful condensed responses to the user's input.
    """),

    MessagesPlaceholder(variable_name="messages"),

    ("human", "{user_input}"),
])

# create a chain including an output parser that will make the AI response more readable
chain = prompt | llm | StrOutputParser()

# create a chat history to store the messages
chat_history = ChatMessageHistory()

# start the chat loop
while True:

    # get user input
    user_input = input("\n\nInput: ")

    # exit the chat loop if the user types "exit"
    if user_input == "exit":
        break

    # create a list to store the AI response
    response = []

    print(f"\nAI Response:")

    # print the AI response as it comes in
    for chunk in chain.stream({"user_input": user_input, "messages": chat_history.messages}):
        print(chunk, end="", flush=True)
        response.append(chunk)

    # join the AI response chunks into a single string
    full_ai_response = "".join(response)

    # add the user input and AI response to the chat history
    chat_history.add_user_message(message=user_input)
    chat_history.add_ai_message(message="".join(full_ai_response))