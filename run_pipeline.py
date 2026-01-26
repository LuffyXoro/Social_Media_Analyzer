# all the code for running the pipeline
# importing necessary modules
import pandas as pd
from data_collection.yt_api import fetch_comments
from preprocessing.clean_text import json_to_dataframe, clean_text
from sentiment.inference import predict_sentiment
from analysis.trend_analysis import (keyword_frequency,
                                        keyword_by_sentiment)

from analysis.time_trends import (sentiment_over_time,
                                  sentiment_ratio_over_time,
                                  keyword_trends_over_time)


def run(video_id):
    data=fetch_comments(video_id)
    if data is None:
        return "Failed to fetch comments." 
    df=json_to_dataframe(data)
    df['cleaned_comment']=df['comment'].apply(clean_text)
    df['sentiment']=df['cleaned_comment'].apply(predict_sentiment)
    df['published_at']=pd.to_datetime(df['published_at'])
    df['date']=df['published_at'].dt.date

    print(df.head())


    print(keyword_frequency(df['cleaned_comment'],top_n=20))
    print("\nTop keywords in negative comments:")
    print(keyword_by_sentiment(df,sentiment_label='neg',top_n=10))
    print('\nSentiment over time:')
    print(sentiment_over_time(df))
    print('\nSentiment ratio over time:')
    print(sentiment_ratio_over_time(df))
    return df # bcz the dashboard expects data to be returned

if __name__=='__main__':
    video_id="J6qIzKxmW8Y"
    run(video_id)

    



    
