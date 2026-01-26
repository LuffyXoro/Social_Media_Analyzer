
from collections import Counter
import pandas as pd


STOPWORDS = set([
    'the','is','and','to','a','of','in','for','on','this','that',
    'it','with','as','are','was','but','be','have','you','i'
])

def keyword_frequency(cleaned_comments, top_n=20):
    words = []
    for comment in cleaned_comments:
        if isinstance(comment, str):
            for word in comment.split():
                if word not in STOPWORDS and len(word) > 2:
                    words.append(word)
    return Counter(words).most_common(top_n)

def keyword_by_sentiment(df, sentiment_label, top_n=10):
    subset = df[df['sentiment'] == sentiment_label]['cleaned_comment']
    words = []
    for comment in subset:
        for word in comment.split():
            if word not in STOPWORDS and len(word) > 2:
                words.append(word)
    return Counter(words).most_common(top_n)

if __name__ == "__main__":
    data = {
        'cleaned_comment': [
            'I love this product',
            'This is the worst service ever',
            'Amazing experience and great value',
            'Not worth the money',
            'Absolutely fantastic quality'
        ],
        'sentiment': ['pos', 'neg', 'pos', 'neg', 'pos']
    }
    df = pd.DataFrame(data)

    print("Overall Top Keywords:")
    print(keyword_frequency(df['cleaned_comment'], top_n=5))

    print("\nTop Positive Keywords:")
    print(keyword_by_sentiment(df, 'pos', top_n=5))

    print("\nTop Negative Keywords:")
    print(keyword_by_sentiment(df, 'neg', top_n=5))

