from scripts.RetrievalQA import Retrieval_QA
import time


qa = Retrieval_QA()
def Final_function(Question):
    t0 = time.time()
    generated_text = qa(Question)
    t1 = time.time()
    latency = t1 - t0
    return generated_text, latency


if __name__ == "__main__":
    question = 'dell'
    Rsponse, latency = Final_function(question)
    print("Latency","="*170)
    print(latency)
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