import pandas as pd

def json_to_dataframe(json_data):
    comments = []
    
    for item in json_data['items']:
        snippet=item['snippet']['topLevelComment']['snippet']
        comments.append(snippet['textDisplay'])
    return pd.DataFrame(comments, columns=['comment'])
