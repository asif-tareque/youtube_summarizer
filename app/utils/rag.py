from langchain.text_splitter import RecursiveCharacterTextSplitter 
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.prompts import PromptTemplate


def chunk_transcript(processed_transcript, chunk_size=200, chunk_overlap=20):
    # Initialize the RecursiveCharacterTextSplitter with specified chunk size and overlap
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap
    )

    # Split the transcript into chunks
    chunks = text_splitter.split_text(processed_transcript)
    return chunks



def create_faiss_index(chunks, embedding_model=None):
    # Create embeddings for each chunk using the provided embedding model
    if embedding_model is None:
        embedding_model = OpenAIEmbeddings(
            model="text-embedding-3-small"
        )
    faiss_index = faiss_index = FAISS.from_texts(chunks, embedding_model)
    return faiss_index

def create_summary_prompt():
    template = """
You are an expert AI assistant that summarizes YouTube video transcripts.

Your goals:
- Extract the core message of the video
- Remove filler, repetition, and transcription noise
- Preserve meaning and context
- Do NOT hallucinate or invent information

Instructions:
1. Write a concise and clear paragraph summary.
2. Extract exactly 5 key points.
3. Provide up to 3 actionable insights if present.
4. Ignore timestamps, speaker labels, and formatting noise.
5. If the transcript is messy, still produce a faithful summary.

Return VALID JSON only:
{{
  "summary": "string",
  "key_points": ["string", "string", "string", "string", "string"],
  "action_items": ["string", "string", "string"]
}}

Transcript:
{transcript}
"""
    return PromptTemplate(
        input_variables=["transcript"],
        template=template
    )


