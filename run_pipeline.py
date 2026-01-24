# all the code for running the pipeline
# importing necessary modules

from data_collection.yt_api import fetch_comments
from preprocessing.clean_text import json_to_dataframe, clean_text
from sentiment.model import predict_sentiment
from analysis.trend_analysis import (keyword_frequency,
                                        keyword_by_sentiment)


def run(video_id):
    data=fetch_comments(video_id)
    if data is None:
        return "Failed to fetch comments." 
    df=json_to_dataframe(data)
    df['cleaned_comment']=df['comment'].apply(clean_text)
    df['sentiment']=df['cleaned_comment'].apply(predict_sentiment)

    print(keyword_frequency(df['cleaned_comment'],top_n=20))
    print("\nTop keywords in negative comments:")
    print(keyword_by_sentiment(df,sentiment_label='negative',top_n=10))
    return df # bcz the dashboard expects data to be returned

# if __name__=='__main__':
#     video_id="PD_VjO99LLw"
#     run(video_id)



    
