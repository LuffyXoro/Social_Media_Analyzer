import pandas as pd

# JSON TO DATAFRAME FUNCTION

def json_to_dataframe(items):
    records = []

    if not isinstance(items, list):
        return pd.DataFrame()

    for item in items:
        try:
            snippet = item["snippet"]["topLevelComment"]["snippet"]
            records.append({
                "comment": snippet.get("textDisplay", ""),
                "likes": snippet.get("likeCount", 0),
                "published_at": snippet.get("publishedAt", "")
            })
        except (KeyError, TypeError):
            continue

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


