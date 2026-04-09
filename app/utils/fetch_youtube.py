from youtube_transcript_api import YouTubeTranscriptApi
import re

ytt_api = YouTubeTranscriptApi()


def get_video_id(url):
    # Regular expression to match YouTube video URLs and extract the video ID
    pattern = r'https:\/\/www\.youtube\.com\/watch\?v=([a-zA-Z0-9_-]{11})'
    match = re.search(pattern, url)
    return match.group(1) if match else None

def get_transcript(video_url):
    video_id = get_video_id(video_url)
   
    if video_id:
        try:
            transcripts = ytt_api.fetch(video_id)
            

            # # Check if the transcript's language is English
            # if transcripts.language_code == 'en':
            #     if transcripts.is_generated:
            #         # If no transcript has been set yet, use the auto-generated one
            #         if len(transcript) == 0:
            #             transcript = transcripts.fetch()
            #     else:
            #         # If a manually created transcript is found, use it (overrides auto-generated)
            #         transcript = transcripts.fetch()
                   
            return transcripts.snippets
        except Exception as e:
            print(f"Error fetching transcript: {e}")
            return None
    else:
        print("Invalid YouTube URL")
        return None
    
def preprocesstranscript(transcript):
    # Prepare the transcript items as textual content

    cleaned_transcript = ""
    for item in transcript: 
        cleaned_transcript +=  f"Text: {item.text} Start: {item.start}\n"
    return cleaned_transcript