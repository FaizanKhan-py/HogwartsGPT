from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader("../data/HarryPotterAndThePhilosophersStone.pdf")

docs = loader.load()

print("Total number of pages: \n", len(docs))
print("4th document object data: \n", docs[3].page_content)