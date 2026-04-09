from langchain.text_splitter import RecursiveCharacterTextSplitter 
from langchain_openai import OpenAIEmbeddings
import faiss


def chunk_transcript(processed_transcript, chunk_size=200, chunk_overlap=20):
    # Initialize the RecursiveCharacterTextSplitter with specified chunk size and overlap
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap
    )

    # Split the transcript into chunks
    chunks = text_splitter.split_text(processed_transcript)
    return chunks

def create_embeddings(chunks, embedding_model=None):
    # Create embeddings for each chunk using the provided embedding model
    if embedding_model is None:
        embedding_model = embeddings = OpenAIEmbeddings(
    model="text-embedding-3-small"  
)
    embeddings = embedding_model.embed_documents(chunks)
    return embeddings

def create_faiss_index(chunks, embedding_model):
   
    # Use the FAISS library to create an index from the provided text chunks
    return faiss.from_texts(chunks, embedding_model)
