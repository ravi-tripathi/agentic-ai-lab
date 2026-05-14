import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

#1 loading api key from .env
load_dotenv()

#2 initialize llm
llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

#3 define first prompt for summary
prompt1 = ChatPromptTemplate.from_template(
    "You are a technical researcher. Provide a 2 sentence summary of: {topic}"
)

#4 define prompt 2 for a 5year old kinda explainer (ELI5)
prompt2 = ChatPromptTemplate.from_template(
    "Take this technical summary: {summary}. Now explain it to a 5-year-old in one simple sentence."
)

#5 Build the chain using LCEL (LangChain Expression Language)

chain1 = prompt1 | llm | StrOutputParser()

chain2 = (
    {"summary" : chain1}
    | prompt2
    | llm
    | StrOutputParser()
)

#6 Test with an example

input_topic = "Quantum Key Distribution in Satellite Communication"
print(f"... Researching : {input_topic}...")

result = chain2.invoke({"topic": input_topic})

print("\nFINAL ELI5 EXPLANATION:")
print(result)