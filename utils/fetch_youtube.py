from youtube_transcript_api import YouTubeTranscriptApi
import re

ytt_api = YouTubeTranscriptApi()
print(ytt_api.fetch("iGeXGdYE7UE"))

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
            transcript = ""
            for t in transcripts:
                # Check if the transcript's language is English
                if t.language_code == 'en':
                    if t.is_generated:
                        # If no transcript has been set yet, use the auto-generated one
                        if len(transcript) == 0:
                            transcript = t.fetch()
                    else:
                        # If a manually created transcript is found, use it (overrides auto-generated)
                        transcript = t.fetch()
                        break
            return transcript
        except Exception as e:
            print(f"Error fetching transcript: {e}")
            return None
    else:
        print("Invalid YouTube URL")
        return None