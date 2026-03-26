from youtube_transcript_api import YouTubeTranscriptApi
import re

ytt_api = YouTubeTranscriptApi()
print(ytt_api.fetch("iGeXGdYE7UE"))

def get_video_id(url):
    # Regular expression to match YouTube video URLs and extract the video ID
    pattern = r'https:\/\/www\.youtube\.com\/watch\?v=([a-zA-Z0-9_-]{11})'
    match = re.search(pattern, url)
    return match.group(1) if match else None
