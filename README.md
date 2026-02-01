# YouTube Comment Sentiment & Trend Analyzer

## Overview
An end-to-end data analytics pipeline that collects YouTube comments,
performs sentiment analysis, extracts keyword insights, and visualizes
time-based trends using an interactive dashboard.

## Architecture
- Data Collection: YouTube Data API
- Preprocessing: Text cleaning & normalization
- Sentiment Analysis: TF-IDF + Logistic Regression
- Analytics: Keyword & time-based trend analysis
- Visualization: Streamlit dashboard

## Features
- Sentiment classification with confidence scores
- Keyword frequency & sentiment-based keyword analysis
- Time-series sentiment trends
- Interactive filtering and CSV export

## Tech Stack
Python, Pandas, Scikit-learn, NLTK, Streamlit, REST APIs, Docker

## Setup Instructions
```bash
pip install -r requirements.txt
streamlit run ui.py
