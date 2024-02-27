# Chatbot - LangChain Ollama

## Description

A series of simple chatbots that can be used to demonstrate the use of the LangChain API and Ollama.

## Requirements

- Python 3.12 or higher
- Ollama server, see https://ollama.com/
- Local model in Ollama, see https://ollama.com/library

    ```
    ollam run <model name>
    ```
- .env (see the **Environment Variables** section)


## Environment Variables.
These projects read the Ollama server and model from environment variables.

Create a file in the project root called `.env` and add the following variables:
```
OLLAMA_HOST: <ollama server> (default: http://localhost:11434)
OLLAMA_MODEL: <model name>
```

**DO NOT COMMIT THE .env FILE**

## Installation

1. Clone the repository
2. Create a python virtual environment
3. Install the requirements `pip install -r requirements.txt`
4. Run a chatbot `python <chatbot>.py`





## List of chatbots

**01.simple_chat.py**

- A simple chatbot that can be used to demonstrate the use of the LangChain API and Ollama. *It has no conversation history.*

**02.state_capitals.py**

- Allow the user to enter a state and respond with the capital.

**03.python_assistant.py**

- Pre-instructed to answer questions about Python.

**04.chat_history.py** 

- Keep track of the chat history so that follow up questions can be asked.

**05.tasks_and_categories.py** 

- Enter tasks and have the chatbot categorize them and respond with the full list of tasks and categories.