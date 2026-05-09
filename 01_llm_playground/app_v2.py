import os
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI

# Prompt Templates
# In real-world Agentic AI, you never hardcode strings like llm.invoke("Hello"). 
# You use Prompt Templates to make your AI logic reusable and modular.

#loading API key from .env
load_dotenv()

#initializing the Gemini Model
llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

# 2. Create a Template
# This allows you to define a "System" role (personality) and "User" input
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are an expert AI Architect specializing in large-scale infrastructure in India."),
    ("user", "Explain the concept of {topic} in the context of {context}.")
])

# 3. Create a Simple Chain (The | symbol is the 'pipe' operator)
chain = prompt | llm

# 4. Invoke with variables
response = chain.invoke({
    "topic": "Data Sovereignty",
    "context": "Digital Public Infrastructure like UPI"
})

print(response.content)


