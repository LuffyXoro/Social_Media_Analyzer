# all the code for running the pipeline
# importing necessary modules

import os
import pandas as pd
from data_collection.yt_api import fetch_comments
from preprocessing.clean_text import json_to_dataframe, clean_text
from sentiment.inference import predict_sentiment_confidence
from analysis.keyword_analysis import (keyword_frequency,
                                        keyword_by_sentiment)

from analysis.sentiment_trends import (sentiment_over_time,
                                  sentiment_ratio_over_time,)

from utils.logger import logger
from utils.paths import RAW_DIR, PROCESSED_DIR

def run(video_id):
    logger.info(f"Pipeline started for video_id={video_id}")


    # step - 1 : Fetching data

    data=fetch_comments(video_id)
    if data is None:
        return "Failed to fetch comments." 
    
    print(type(data))
    print(data)
    
    #step - 2 : JSON -> Df

    # step - 2 : JSON -> Df
    items = data.get("items", [])
    df = json_to_dataframe(items)

    if df.empty:
        return "No comments found for this video."

    
    #step - 3 : Text cleaning and storing intermediate results
    

    df.to_csv(RAW_DIR / "comments.csv", index=False)

    df["cleaned_comment"] = df["comment"].apply(clean_text)
    df.to_csv(PROCESSED_DIR / "cleaned_comments.csv", index=False)

    # step - 4 : Sentiment Prediction

    df[["sentiment", "confidence"]] = df["cleaned_comment"].apply(lambda x: pd.Series(predict_sentiment_confidence(x)))

    # step - 5 : Additional preprocessing

    df['published_at']=pd.to_datetime(df['published_at'])
    df['date']=df['published_at'].dt.date

    # Results
    logger.info("Comments fetched successfully")
    logger.info(f"Total comments: {len(df)}")

    logger.info(f"Raw data saved to {RAW_DIR / 'comments.csv'}")
    logger.info(f"Processed data saved to {PROCESSED_DIR / 'cleaned_comments.csv'}")

    # print("\nTop 20 Keywords:")
    # print(keyword_frequency(df['cleaned_comment'],top_n=20))

    # print("\nTop keywords in negative comments:")
    # print(keyword_by_sentiment(df,sentiment_label='neg',top_n=10))

    # print('\nSentiment over time:')
    # print(sentiment_over_time(df))

    # print('\nSentiment ratio over time:')
    # print(sentiment_ratio_over_time(df))

    logger.info("Pipeline finished successfully")

    
    return df # bcz the dashboard expects data to be returned




    



    
