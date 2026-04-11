import utils.fetch_youtube as fetch_youtube
import utils.rag as rag
from dotenv import load_dotenv
import os

load_dotenv()

transcript = fetch_youtube.get_transcript("https://www.youtube.com/watch?v=iGeXGdYE7UE")


transcript = fetch_youtube.preprocesstranscript(transcript)
chunks = rag.chunk_transcript(transcript)

faiss_index = rag.create_faiss_index(chunks)
print(faiss_index)
