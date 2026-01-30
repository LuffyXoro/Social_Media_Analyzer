import streamlit as st
import pandas as pd

from dashboard.data_provider import get_dashboard_data

st.set_page_config(
    page_title="YouTube Sentiment Dashboard",
    layout="wide"
)

st.title("📊 YouTube Comment Sentiment Analysis")

if "data" not in st.session_state:
    st.session_state.data = None

if "daily_pct" not in st.session_state:
    st.session_state.daily_pct = None

video_id = st.text_input(
    "Enter YouTube Video ID",
    placeholder="e.g. PD_VjO99LLw"
)

if st.button("Analyze") and video_id:
    with st.spinner("Fetching and analyzing comments..."):
        st.session_state.data = get_dashboard_data(video_id)

if st.session_state.data is None:
    st.info("Enter a video ID and click Analyze")
    st.stop()

data = st.session_state.data

if "error" in data:
    st.error(data["error"])
    st.stop()

df = data["raw_df"].copy()
df["date"] = pd.to_datetime(df["date"]).dt.date

daily = (
    df
    .groupby(["date", "sentiment"])
    .size()
    .unstack(fill_value=0)
)

daily_pct = daily.div(daily.sum(axis=1), axis=0)
st.session_state.daily_pct = daily_pct

col1, col2, col3 = st.columns(3)
col1.metric("Total Comments", data["total_comments"])
col2.metric("Positive (%)", data["positive_pct"])
col3.metric("Negative (%)", data["negative_pct"])

st.divider()

st.subheader("🔍 Filters")

min_date = daily_pct.index.min()
max_date = daily_pct.index.max()

start_date, end_date = st.date_input(
    "Select date range",
    value=(min_date, max_date),
    min_value=min_date,
    max_value=max_date
)

sentiment_choice = st.multiselect(
    "Select sentiment",
    options=["pos", "neg"],
    default=["pos", "neg"]
)

st.divider()

st.subheader("📈 Sentiment Trend Over Time")

trend_data = st.session_state.daily_pct.loc[start_date:end_date]

if sentiment_choice:
    trend_data = trend_data[sentiment_choice]
else:
    st.stop()

st.line_chart(trend_data)

st.subheader("💬 Comments")

filtered_df = df[
    (df["date"] >= start_date) &
    (df["date"] <= end_date) &
    (df["sentiment"].isin(sentiment_choice))
]

st.dataframe(
    filtered_df[["date", "sentiment", "comment"]],
    use_container_width=True
)

st.bar_chart(df["sentiment"].value_counts())

st.subheader("📝 Sentiment Summary")

st.subheader("⬇️ Download Reports")

full_csv = df.to_csv(index=False).encode("utf-8")
filtered_csv = filtered_df.to_csv(index=False).encode("utf-8")

col_dl1, col_dl2 = st.columns(2)

col_dl1.download_button(
    "Download Full Data (CSV)",
    data=full_csv,
    file_name="youtube_sentiment_full.csv",
    mime="text/csv"
)

col_dl2.download_button(
    "Download Filtered Data (CSV)",
    data=filtered_csv,
    file_name="youtube_sentiment_filtered.csv",
    mime="text/csv"
)
