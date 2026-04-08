import utils.fetch_youtube as fetch_youtube
import utils.rag as rag


transcript = fetch_youtube.get_transcript("https://www.youtube.com/watch?v=iGeXGdYE7UE")


transcript = fetch_youtube.preprocesstranscript(transcript)
chunks = rag.chunk_transcript(transcript)
print(chunks)