#from langchain.embeddings import HuggingFaceEmbeddings
#from langchain_community.embeddings import HuggingFaceEmbeddings
#from langchain.vectorstores import Chroma
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

from LoadPDF import LoadPdf
from Chunking import Chunking_Text 

def Save_chromadb(Chunks):
    try:
        model_name = "BAAI/bge-m3"
        model_kwargs = {"device": "cpu"}
        encode_kwargs = {"normalize_embeddings": True}

        embeddings = HuggingFaceEmbeddings(
            model_name=model_name,
            model_kwargs=model_kwargs,
            encode_kwargs=encode_kwargs,
        )

        vectorstore = Chroma.from_documents(
            documents=Chunks,
            embedding=embeddings,
            persist_directory="chroma_index",
        )

        vectorstore.persist()
        print("Chroma is saved with succes")
    except Exception as e:
        print("we have some error", e)

if __name__ == "__main__":
    pages = LoadPdf("./Data/Data.pdf")
    chunks = Chunking_Text(pages)
    Save_chromadb(chunks)