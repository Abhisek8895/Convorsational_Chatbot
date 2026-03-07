from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from django.conf import settings
from dotenv import load_dotenv
import os

load_dotenv()

# Initialize the LLM
llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0,
    api_key=os.getenv('GROQ_API_KEY')
)


# System prompt
system_prompt = """
You are a helpful AI assistant.
Use the chat history to understand the conversation context
and respond clearly and helpfully.
"""


# Prompt template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system_prompt),
        MessagesPlaceholder("chat_history"),
        ("human", "{input}")
    ]
)


# Create the chain
chain = prompt | llm


def generate_ai_response(chat_history, user_input):
    """
    Generate AI response using chat history and user input.

    chat_history: list of LangChain messages
    user_input: latest user message
    """

    response = chain.invoke({
        "chat_history": chat_history,
        "input": user_input
    })

    return response.content