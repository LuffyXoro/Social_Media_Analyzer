
from collections import Counter
STOPWORDS = set([
    'the','is','and','to','a','of','in','for','on','this','that',
    'it','with','as','are','was','but','be','have','you','i'
])

def keyword_frequency(cleaned_comments, top_n=50):
    all_words = []
    for comment in cleaned_comments:
        if isinstance(comment, str):
            words = [
                word for word in comment.split()
                if word not in STOPWORDS and len(word) > 2
            ]
            all_words.extend(words)

    return Counter(all_words).most_common(top_n)

def keyword_by_sentiment(df,sentiment_label='negative',top_n=10):
    subset=df[df['sentiment']==sentiment_label]
    return keyword_frequency(subset['cleaned_comment'],top_n)



