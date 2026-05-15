import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

# --- PROMPT 1 ---
prompt1 = ChatPromptTemplate.from_template("You are a technical researcher. Provide a 2 sentence summary of: {topic}")

# --- PROMPT 2: THE ANALOGY-BASED ELI5 ---
# Note: We provide a "system" role and a "few-shot" example here
prompt2 = ChatPromptTemplate.from_messages([
    ("system", "You are a world-class teacher. You explain complex ideas using simple playground analogies."),
    ("user", """ 
     Here is a technical summary: 'Quantum Key Distribution uses the laws of physics to detect eavesdroppers on a communication line.'
    Explain this to a 5-year-old in one sentence. 
    """),
    ("assistant", "It's like sending a secret note written on a bubble; if a bad guy tries to touch it or read it, the bubble pops and the message vanishes!"),
    ("user", "Now, take this technical summary: {summary}. Explain it to a 5-year-old in one simple sentence using a NEW analogy.")
    
])

# --- prompt chaining ---
chain1 = prompt1 | llm | StrOutputParser()

full_chain = (
    {"summary": chain1} 
    | prompt2 
    | llm 
    | StrOutputParser()
)

# --- testing improved EL15 explanation ---
topic_input = "Quantum Key Distribution in Secure Military communications"
print(f"--- RESEARCHING: {topic_input} ---")

result = full_chain.invoke({"topic": topic_input})

print("\nIMPROVED ELI5 EXPLANATION:")
print(result)