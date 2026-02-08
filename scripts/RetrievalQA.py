#from langchain.chains import RetrievalQA
from langchain.chains.retrieval_qa.base import RetrievalQA

from scripts.Model import Get_Model
from scripts.Retrieve_Data import Get_Retriever
from scripts.Pre_Prompt import Get_Prompt

def Retrieval_QA():
    llm = Get_Model()
    retriever = Get_Retriever()
    prompt = Get_Prompt()
    chain_qa = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        chain_type="stuff",
        chain_type_kwargs={'prompt':prompt},
        return_source_documents=True
    )
    if chain_qa:
        print("RetrievalQA created successfully")
        return chain_qa
    else:
        print("RetrievalQA not created successfully")

if __name__ == "__main__":
    qa = Retrieval_QA()
    question = "Can you tell me what is 'system information'?"
    generated_text = qa(question)
    print(generated_text)
