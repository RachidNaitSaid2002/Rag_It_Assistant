from langchain.embeddings import HuggingFaceEmbeddings

from langchain.vectorstores import Chroma

def Get_Retriever():
    # Objet d'embedding
    embeddings = HuggingFaceEmbeddings(
        model_name = "BAAI/bge-m3",
        model_kwargs = {'device':'cpu'},
        encode_kwargs = {"normalize_embeddings":True}
    )

    # Charger base de données
    vectorstore = Chroma(
        persist_directory="./chroma_index",
        embedding_function=embeddings
    )

    # Retriever
    retriever = vectorstore.as_retriever(
        search_type="similarity",
        search_kwargs={"k":5}
    )
    return retriever

if  __name__ == "__main__":
    retrierver = Get_Retriever()
    print("Nombre de documents :", retrierver.vectorstore._collection.count())
