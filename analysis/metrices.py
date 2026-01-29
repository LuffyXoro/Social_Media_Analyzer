def sentiment_summary(df):
    total = len(df)

    pos = (df["sentiment"] == "pos").sum()
    neg = (df["sentiment"] == "neg").sum()

    return {
        "total_comments": total,
        "positive %": round(pos * 100 / total, 2) if total else 0,
        "negative %": round(neg * 100 / total, 2) if total else 0,
    }

def top_negative_comments(df, n=10):
    return (
        df[df["sentiment"] == "neg"]
        .sort_values(by="date", ascending=False)
        .head(n)[["comment", "date"]]
    )
