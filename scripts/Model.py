from langchain_google_genai import ChatGoogleGenerativeAI
import os
from dotenv import load_dotenv

load_dotenv()

os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")

def Get_Model():
    Model = ChatGoogleGenerativeAI(
        model="gemini-3-flash-preview",
        temperateur=0
    )
    return Model

if __name__ == "__main__":
    Model = Get_Model()
    print(Model)