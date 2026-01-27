from langchain.text_splitter import RecursiveCharacterTextSplitter

def Chunking_Text(pages):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size = 500,
        chunk_overlap = 50,
        separators=["\n\n", "\n","."," ", ""]
    )

    chunks = text_splitter.split_documents(pages)
    return chunks

