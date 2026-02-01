import requests
import os
from dotenv import load_dotenv
from utils.config import config

load_dotenv()

API_KEY = os.getenv("YOUTUBE_API_KEY")
if not API_KEY:
    raise ValueError("YOUTUBE_API_KEY not found in .env file")

BASE_URL = "https://www.googleapis.com/youtube/v3/commentThreads"
MAX_RESULTS = config["yt_api"]["max_results"]

def fetch_comments(video_id):
    comments = []
    next_page_token = None

    while True:
        params = {
            "part": "snippet",
            "videoId": video_id,
            "maxResults": MAX_RESULTS,
            "key": API_KEY,
        }

        if next_page_token:
            params["pageToken"] = next_page_token

        response = requests.get(BASE_URL, params=params)

        if response.status_code != 200:
            print("Error fetching comments:", response.text)
            break

        data = response.json()
        comments.extend(data.get("items", []))

        next_page_token = data.get("nextPageToken")
        if not next_page_token:
            break

    return comments
