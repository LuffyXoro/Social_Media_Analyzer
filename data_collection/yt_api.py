import requests
import os
from dotenv import load_dotenv


from preprocessing.clean_text import json_to_dataframe
from preprocessing.clean_text import clean_text
from utils.config import config


max_results = config['yt_api']['max_results']

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
    

comments=[]
next_page=None
while True :
    params['pageToken']=next_page

    response=requests.get(BASE_URL,params=params)
    data=response.json()

    comments.extend(data.get('items',[]))
    next_page=data.get('nextPageToken')
    if not next_page:
        break