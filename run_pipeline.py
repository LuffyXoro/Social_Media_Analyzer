# all the code for running the pipeline
# importing necessary modules
import pandas as pd
from data_collection.yt_api import fetch_comments
from preprocessing.clean_text import json_to_dataframe, clean_text
from sentiment.inference import predict_sentiment_confidence
from analysis.keyword_analysis import (keyword_frequency,
                                        keyword_by_sentiment)

from analysis.sentiment_trends import (sentiment_over_time,
                                  sentiment_ratio_over_time,)

from utils.logger import logger




def run(video_id):

    # step - 1 : Fetching data

    data=fetch_comments(video_id)
    if data is None:
        return "Failed to fetch comments." 
    
    #step - 2 : JSON -> Df

    df=json_to_dataframe(data)
    if df.empty:
        return "No comments found for this video."
    
    #step - 3 : Text cleaning and storing intermediate results
    
    df.to_csv("data/raw/comments.csv",index=False)

    df['cleaned_comment']=df['comment'].apply(clean_text)

    df.to_csv("data/processed/cleaned_comments.csv",index=False)

    # step - 4 : Sentiment Prediction

    df[["sentiment", "confidence"]] = df["cleaned_comment"].apply(lambda x: pd.Series(predict_sentiment_confidence(x)))

    # step - 5 : Additional preprocessing

    df['published_at']=pd.to_datetime(df['published_at'])
    df['date']=df['published_at'].dt.date

    # Results

    logger.info("Fetching Comments...")
    logger.info(f"Total Comments Fetched: {len(df)}")

    print("\nTop 20 Keywords:")
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



    



    
