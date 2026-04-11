import utils.fetch_youtube as fetch_youtube
import utils.rag as rag
import utils.prompts as prompts
from dotenv import load_dotenv
import os
from openai import OpenAI
import json


load_dotenv()

transcript = fetch_youtube.get_transcript("https://www.youtube.com/watch?v=iGeXGdYE7UE")


transcript = fetch_youtube.preprocesstranscript(transcript)
chunks = rag.chunk_transcript(transcript)

faiss_index = rag.create_faiss_index(chunks)


client = OpenAI()

def run_summary(prompt: str):
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {
                "role": "system",
                "content": "You are an expert AI assistant that summarizes YouTube transcripts and returns valid JSON only."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.2,
    )

    content = response.choices[0].message.content
    return json.loads(content)

summary_prompt = prompts.create_summary_prompt().format(transcript=transcript)

summary = run_summary(summary_prompt)
print(summary)