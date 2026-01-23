# all the code for running the pipeline
# importing necessary modules

from data_collection.yt_api import fetch_comments
from preprocessing.clean_text import json_to_dataframe, clean_text
from sentiment.model import predict_sentiment
from analysis.trend_analysis import (keyword_frequency,
                                        keyword_by_sentiment)




