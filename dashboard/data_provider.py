from run_pipeline import run

def get_dashboard_data(video_id):
    df = run(video_id)

    if isinstance(df, str):
        return {"error": df}

    sentiment_counts = df['sentiment'].value_counts().to_dict()
    total_comments = len(df)

    positive_pct = round(
        sentiment_counts.get('pos', 0) / total_comments * 100, 2
    ) if total_comments else 0

    negative_pct = round(
        sentiment_counts.get('neg', 0) / total_comments * 100, 2
    ) if total_comments else 0

    sentiment_trend = (
        df.groupby(['date', 'sentiment'])
        .size()
        .unstack(fill_value=0)
    )

    top_negative_comments = (
        df[df['sentiment'] == 'neg']
        .sort_values(by='date', ascending=False)
        .head(10)[['comment', 'date']]
    )

    return {
        "raw_df": df,
        "total_comments": total_comments,
        "positive_pct": positive_pct,
        "negative_pct": negative_pct,
        "sentiment_counts": sentiment_counts,
        "sentiment_trend": sentiment_trend,
        "top_negative_comments": top_negative_comments
    }
