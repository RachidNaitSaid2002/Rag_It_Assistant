from langchain.text_splitter import RecursiveCharacterTextSplitter
from scripts.LoadPDF import LoadPdf

def Chunking_Text(pages):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size = 500,
        chunk_overlap = 50,
        separators=["\n\n", "\n","."," ", ""]
    )

    chunks = text_splitter.split_documents(pages)
    if chunks:
        print("Chunks created successfully")
        return chunks
    else:
        print("Chunks not created successfully")

if __name__ == "__main__":
    pages = LoadPdf("./Data/Data.pdf")
    chunks = Chunking_Text(pages)
    print(len(chunks))