import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from pydantic import BaseModel, Field

#loading API key from .env
load_dotenv()

#defining the Schema for {"concept": "string", "importance_score": 1-10, "key_takeaway": "string"}

class StructuredOutput(BaseModel):
    concept: str = Field(description="A topic that needs explanation")
    importance_score: int = Field(description="A score between 1 to 10 determining the importance of the topic")
    key_takeaway: str = Field(description="Most Important learning")

#initialize llm model
llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

#Getting to the structured output

structured_llm = llm.with_structured_output(StructuredOutput)

#Invoking the LLM

response = structured_llm.invoke("Explain neural networks")
print(f"Concept: {response.concept}")
print(f"Importance Score: {response.importance_score}")
print(f"Key Takeaway: {response.key_takeaway}")