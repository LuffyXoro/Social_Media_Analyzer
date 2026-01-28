def sentiment_over_time(df):
    return (
        df.groupby(['date', 'sentiment']).size().unstack(fill_value=0)
    )

def sentiment_ratio_over_time(df):
    daily = df.groupby('date')['sentiment'].value_counts(normalize=True)
    return daily.unstack(fill_value=0) * 100

def keyword_trends_over_time(df, keyword):
    df['contains_keyword'] = df['cleaned_comment'].apply(
        lambda x: keyword in x.split()
    )
    daily_counts = df.groupby(['date', 'contains_keyword']).size().unstack(fill_value=0)
    return daily_counts

