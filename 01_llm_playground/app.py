import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

#loading API key from .env
load_dotenv()

#initializing the Gemini Model
llm = ChatGoogleGenerativeAI(model="gemini-3-flash-preview")

#simple llm invocation
response = llm.invoke("Explain AI agents, Agentic AI and their uses in one paragraph")

print(response.content)