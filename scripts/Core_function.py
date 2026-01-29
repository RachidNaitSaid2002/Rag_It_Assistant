from RetrievalQA import Retrieval_QA

def Final_function(Question):
    qa = Retrieval_QA()
    generated_text = qa(Question)
    return generated_text


if __name__ == "__main__":
    question = 'What does Mike Halsey recommend as the best IT support tool released in 2019?'
    Rsponse = Final_function(question)
    print("Query","="*170)
    print(Rsponse['query'])
    print("Result","="*170)
    print(Rsponse['result'])
    if Rsponse['result'] != "Je ne trouve pas l'information dans le contexte fourni.":
        print("Source","="*170)
        for doc in Rsponse['source_documents']:
            print(f"****** Page :",doc.metadata["page"])
            print(f"****** file Source :",doc.metadata["source"])
            print(f"****** page content :",doc.page_content)