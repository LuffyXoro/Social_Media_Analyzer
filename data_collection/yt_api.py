import requests
import os
from dotenv import load_dotenv

# load .env file
load_dotenv()

API_KEY = os.getenv("YOUTUBE_API_KEY")

if not API_KEY:
    raise ValueError("YOUTUBE_API_KEY not found in .env file")

BASE_URL = "https://www.googleapis.com/youtube/v3/commentThreads"

def fetch_comments(video_id, max_results=50):
    params = {
        'part': 'snippet',
        'videoId': video_id,
        'maxResults': max_results,
        'key': API_KEY
    }

    response = requests.get(BASE_URL, params=params)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error fetching comments: {response.status_code}")
        return None

if __name__=="__main__":
    video_id="PD_VjO99LLw"
    data=fetch_comments(video_id)

    if data:
        print("Keys in response:",data.keys())
        print("/n")
        print("First sample: ",data["items"][0])