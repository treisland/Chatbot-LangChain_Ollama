import os

from dotenv import load_dotenv
from langchain.chains import LLMChain
from langchain_community.chat_models import ChatOllama
from langchain_core.prompts import ChatPromptTemplate, PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.memory import ConversationBufferMemory

load_dotenv()

llm = ChatOllama(model=os.getenv("OLLAMA_MODEL"))

prompt_template = ("Tell a story about two characters, {character1} and {character2}."
                   "The theme is {theme}")

prompt = PromptTemplate(input_variables=["x", "y"], template=prompt_template)

chain = prompt | llm | StrOutputParser()

print("Assistant: Welcome to the story generator! I will help you create a story about two characters and a theme.")

name1 = input("\n\nCharacter 1: ")
name2 = input("\nCharacter 2: ")
theme = input("\nTheme: ")

print("\nStory: ", end="", flush=True)

for chunk in chain.stream(input={"character1": name1, "character2": name2, "theme": theme}):
    print(chunk, end="", flush=True)
