from langchain_community.document_loaders import PyPDFLoader

# Load Pdf
def LoadPdf(pdf_path : str):
    loader = PyPDFLoader(pdf_path)
    pages = loader.load()
    # i = 4
    # print(f"--- Page {i + 1} ---")
    # print(f"Content Sample: {pages[i].page_content}") 
    # print(f"Metadata:")
    # pprint.pprint(pages[i].metadata)
    # print("-" * 20)
    # --------------------------------------------------------
    # for i, page in enumerate(pages):
    #     print(f"--- Page {i + 1} ---")
    #     print(f"Content Sample: {page.page_content[:200]}...") 
    #     print(f"Metadata:")
    #     pprint.pprint(page.metadata)
    #     print("-" * 20)
    if pages:
        print("Pdf loaded successfully")
        return pages
    else:
        print("Pdf not loaded successfully")

if __name__ == "__main__":
    pages = LoadPdf("./Data/Data.pdf")

