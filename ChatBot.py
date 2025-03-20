from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv


load_dotenv()

model=ChatGoogleGenerativeAI(model='gemini-1.5-pro')
chat_history=[]
while True:
    user_input = input("User: ")
    chat_history.append(user_input)
    if user_input == 'exit':
        break
    result=model.invoke(chat_history)
    chat_history.append(result)
    print('AI: ',result.content)