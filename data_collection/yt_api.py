# Handles data ingestion from the YouTube Data API and returns raw comment JSON.


import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("YOUTUBE_API_KEY")
BASE_URL = "https://www.googleapis.com/youtube/v3/commentThreads"


def fetch_comments(video_id, max_results=100):
    all_items = []
    next_page_token = None

    while True:
        params = {
            "part": "snippet",
            "videoId": video_id,
            "maxResults": max_results,
            "pageToken": next_page_token,
            "key": API_KEY,
        }

        try:
            response = requests.get(
                BASE_URL,
                params=params,
                timeout=10
            )
            response.raise_for_status()
            data = response.json()

        except requests.exceptions.RequestException as e:
            print(f"[YT API ERROR] {e}")
            break   # graceful exit, not crash

        items = data.get("items", [])
        all_items.extend(items)

        next_page_token = data.get("nextPageToken")
        if not next_page_token:
            break

    return {
        "items": all_items
    }
