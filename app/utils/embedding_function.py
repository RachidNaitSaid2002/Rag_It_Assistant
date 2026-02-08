from langchain_huggingface import HuggingFaceEmbeddings


model_name = "BAAI/bge-m3"
embeddings = HuggingFaceEmbeddings(
    model_name=model_name,
    model_kwargs={"device": "cpu"},
    encode_kwargs={"normalize_embeddings": True},
)

def get_embedding(Question):
    Vector = embeddings.embed_query(Question)
    return Vector

if __name__ == "__main__":
    print(get_embedding("Hello"))

