from langchain.chains import RetrievalQA

from Model import Get_Model
from Retrieve_Data import Get_Retriever
from Pre_Prompt import Get_Prompt

def Retrieval_QA(llm, retriever,prompt):
    chain_qa = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        chain_type="stuff",
        chain_type_kwargs={'prompt':prompt}
    )
    return chain_qa

if __name__ == "__main__":
    llm = Get_Model()
    retriever = Get_Retriever()
    prompt = Get_Prompt()
    chain = Retrieval_QA(llm, retriever, prompt)
    print(chain)
