import pandas as pd

# JSON TO DATAFRAME FUNCTION

def json_to_dataframe(items):
    records = []

    for item in items:
        snippet = item["snippet"]["topLevelComment"]["snippet"]

        records.append({
            "comment": snippet["textDisplay"],
            "published_at": snippet["publishedAt"],
            "likes": snippet["likeCount"]
        })

    return pd.DataFrame(records)


# CLEANING TEXT FUNCTIONS

import re 

def clean_text(text):
    text = re.sub(r'http\S+|www\S+|https\S+', '', text, flags=re.MULTILINE)
    text = re.sub(r'<.*?>', '', text)
    text = re.sub(r'[^A-Za-z\s]', '', text)
    text = text.lower()
    text = re.sub(r'\s+', ' ', text).strip()
    
    return text


