from document_loader import docs
from langchain_text_splitters import RecursiveCharacterTextSplitter

splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)

chunks = splitter.split_documents(docs)

print("Total Chunks:", len(chunks))
print("First Chunk:", chunks[0].page_content)
print("Metadata:", chunks[0].metadata)