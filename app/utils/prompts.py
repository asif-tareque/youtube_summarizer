
from langchain.prompts import PromptTemplate

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