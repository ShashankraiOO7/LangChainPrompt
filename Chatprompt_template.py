from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import GoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()
model =GoogleGenerativeAI(model='gemini-1.5-pro')
chat_template = ChatPromptTemplate([
    ('system', 'You are a helpful {domain} expert'),
    ('human', 'Explain in simple terms, what is {topic}')
])

domain=input("Enter Domain")
topic=input("Enter Topic")

prompt = chat_template.invoke({'domain':domain,'topic':topic})

print(model.invoke(prompt))