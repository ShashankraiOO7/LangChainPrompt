from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import PromptTemplate,load_prompt
load_dotenv()

model= ChatGoogleGenerativeAI(model='gemini-1.5-pro')

st.header('Reasearch Tool')
result=st.text_input("Enter the Input")

if st.button("Summerize"):
    output=model.invoke(result)
    st.write(output.content)
    