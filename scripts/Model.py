from langchain_google_genai import ChatGoogleGenerativeAI
import os
from dotenv import load_dotenv

load_dotenv()


def Get_Model():
    model = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        temperature=0
    )
    return model

if __name__ == "__main__":
    model = Get_Model()
    print(model)
    print(model.invoke('Say Dima Wydad').content)