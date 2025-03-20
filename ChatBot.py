from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv


load_dotenv()

model=ChatGoogleGenerativeAI(model='gemini-1.5-pro')

while True:
    user_input = input("User: ")
    if user_input == 'exit':
        break
    result=model.invoke(user_input)
    print('AI: ',result.content)