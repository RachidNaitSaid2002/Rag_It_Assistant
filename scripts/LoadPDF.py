from langchain_community.document_loaders import PyPDFLoader
import pprint

loader = PyPDFLoader("./Data/Data.pdf")

pages = loader.load()
i = 20


print(f"--- Page {i + 1} ---")
print(f"Content Sample: {pages[i].page_content}") 
print(f"Metadata:")
pprint.pprint(pages[i].metadata)
print("-" * 20)

# for i, page in enumerate(pages):
#     print(f"--- Page {i + 1} ---")
#     print(f"Content Sample: {page.page_content[:200]}...") 
#     print(f"Metadata:")
#     pprint.pprint(page.metadata)
#     print("-" * 20)
