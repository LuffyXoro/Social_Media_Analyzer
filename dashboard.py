import streamlit as slt
import matplotlib.pyplot as plt
from wordcloud import WordCloud




from analysis.trend_analysis import keyword_frequency, keyword_by_sentiment
from run_pipeline import run



def generate_wordcloud(text):
    wordcloud=WordCloud(width=800,height=400,background_color='black',max_words=100).generate(text)
    plt.figure(figsize=(10,5))
    plt.imshow(wordcloud,interpolation='bilinear')
    plt.axis('off')
    slt.pyplot(plt)


slt.title("YouTube Comments Sentiment Analysis Dashboard")
video_id=slt.text_input("Enter YouTube Video ID:") # Yt's unique video indetifier


if slt.button("Analyze"):
    with slt.spinner('Fetching & analyzing comments...'):
        data=run(video_id)
        if isinstance(data,str):
            slt.error("Recheck the unique video ID: "+data)
        else:
            df=data
            slt.success("Analysis Complete!")
            slt.subheader("Top 5 Keywords Overall")
            top_keywords=keyword_frequency(df['cleaned_comment'],top_n=5)
            for word,count in top_keywords:
                slt.write(f"{word}: {count}")

            slt.subheader("Top 10 Keywords in Negative Comments")
            neg_keywords=keyword_by_sentiment(df,sentiment_label='neg',top_n=10)
            for word,count in neg_keywords:
                slt.write(f"{word}: {count}")

            all_text=" ".join(df['cleaned_comment'].tolist())
            slt.subheader("Word Cloud of Comments")
            generate_wordcloud(all_text)


