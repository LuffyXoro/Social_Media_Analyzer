import pandas as pd


# JSON TO DATAFRAME FUNCTION

def json_to_dataframe(json_data):
    comments = []
    
    for item in json_data['items']:
        snippet=item['snippet']['topLevelComment']['snippet']
        comments.append(snippet['textDisplay'])
    return pd.DataFrame(comments, columns=['comment'])


# CLEANING TEXT FUNCTIONS

import re 

def clean_text(text):
    text = re.sub(r'http\S+|www\S+|https\S+', '', text, flags=re.MULTILINE)
    text = re.sub(r'<.*?>', '', text)
    text = re.sub(r'[^A-Za-z\s]', '', text)
    text = text.lower()
    text = re.sub(r'\s+', ' ', text).strip()
    
    return text


