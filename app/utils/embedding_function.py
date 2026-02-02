from langchain.embeddings import HuggingFaceEmbeddings


model_name = "BAAI/bge-m3"
embeddings = HuggingFaceEmbeddings(
    model_name=model_name,
    model_kwargs={"device": "cpu"},
    encode_kwargs={"normalize_embeddings": True},
)
def embedding_function(Question):
    Vector = embeddings.embed_query(Question)
    return Vector

if __name__ == "__main__":
    print(embedding_function("Hello"))

