from dotenv import load_dotenv
import os
from src.helper import load_pdf_file, filter_to_minimal_docs, text_split, download_hugging_face_embeddings
# from pinecone import Pinecone
from pinecone import Pinecone, ServerlessSpec
from langchain_pinecone import PineconeVectorStore
from langchain_community.document_loaders import PyPDFLoader, DirectoryLoader
from langchain_community.embeddings import HuggingFaceEmbeddings



load_dotenv()


PINECONE_API_KEY=os.environ.get('PINECONE_API_KEY')
GOOGLE_API_KEY=os.environ.get('GOOGLE_API_KEY')

os.environ["PINECONE_API_KEY"] = PINECONE_API_KEY
os.environ["GOOGLE_API_KEY"] = GOOGLE_API_KEY


extracted_data=load_pdf_file(data='data/')
filter_data = filter_to_minimal_docs(extracted_data)
text_chunks=text_split(filter_data)

embeddings = download_hugging_face_embeddings()

pinecone_api_key = PINECONE_API_KEY
pc = Pinecone(api_key=pinecone_api_key)



index_name = "medical-bot"  # change if desired

if index_name not in pc.list_indexes().names():
    pc.create_index(
        name=index_name,
        dimension=384,
        metric="cosine",
        spec=ServerlessSpec(cloud="aws", region="us-east-1")
    )

index = pc.Index(index_name)


docsearch = PineconeVectorStore.from_documents(
    documents=text_chunks,
    index_name=index_name,
    embedding=embeddings, 
)