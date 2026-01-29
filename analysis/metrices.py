def sentiment_summary(df):
    total = len(df)

    pos = (df["sentiment"] == "pos").sum()
    neg = (df["sentiment"] == "neg").sum()

    return {
        "total_comments": total,
        "positive_pct": round(pos * 100 / total, 2) if total else 0,
        "negative_pct": round(neg * 100 / total, 2) if total else 0,
    }

def top_negative_comments(df, n=10):
    return (
        df[df["sentiment"] == "neg"]
        .sort_values(by="date", ascending=False)
        .head(n)[["comment", "date"]]
    )

if __name__ == "__main__":
    import pandas as pd

    data = {
        "comment": [
            "I love this video!",
            "This is terrible.",
            "Great content, very informative.",
            "I hate the way this was presented.",
            "Absolutely fantastic!",
            "Not good at all.",
        ],
        "sentiment": ["pos", "neg", "pos", "neg", "pos", "neg"],
        "date": pd.to_datetime(
            [
                "2023-10-01",
                "2023-10-01",
                "2023-10-02",
                "2023-10-02",
                "2023-10-03",
                "2023-10-03",
            ]
        ),
    }

    df = pd.DataFrame(data)

    summary = sentiment_summary(df)
    print("Sentiment Summary:", summary)

    top_neg = top_negative_comments(df, n=3)
    print("\nTop Negative Comments:\n", top_neg)