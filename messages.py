from langchain_core.messages import SystemMessage,HumanMessage,AIMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model=ChatGoogleGenerativeAI(model='gemini-1.5-pro')

messages=[ SystemMessage(content="You are hair Docter"),
          HumanMessage(content="Any solution to regrow the Hair of my head in 20 wrds only")]

output=model.invoke(messages)
messages.append(output)

print(messages)