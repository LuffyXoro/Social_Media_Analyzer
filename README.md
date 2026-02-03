YOUTUBE COMMENT SENTIMENT & TREND ANALYZER
📌 Overview

An end-to-end data analytics pipeline that collects YouTube comments, performs sentiment analysis, extracts keyword insights, and visualizes time-based trends using an interactive dashboard.
The project supports both local execution and Docker-based containerized deployment for reproducibility.

🏗 Architecture

Data Collection: YouTube Data API

Preprocessing: Text cleaning and normalization

Sentiment Analysis: TF-IDF + Logistic Regression

Analytics: Keyword frequency and time-based sentiment trends

Visualization: Streamlit dashboard

Deployment: Docker

✨ Features

Sentiment classification with confidence scores

Keyword frequency and sentiment-based keyword analysis

Time-series sentiment trend visualization

Interactive Streamlit dashboard

Fully containerized execution using Docker

🧰 Tech Stack

Python, Pandas, Scikit-learn, NLTK, Streamlit, REST APIs, Docker

📂 Project Structure

ui.py – Streamlit UI and dashboard logic

run_pipeline.py – Orchestrates the complete data pipeline

data_collection/ – YouTube API data fetching logic

preprocessing/ – Text cleaning and transformation

sentiment/ – Sentiment inference and trained models

analysis/ – Keyword and trend analysis

utils/ – Logging and shared utilities

Dockerfile – Docker configuration

requirements.txt – Python dependencies

▶️ Local Setup

Install dependencies and run the Streamlit app:

pip install -r requirements.txt
streamlit run ui.py

Access the application at:
http://localhost:8501

🐳 Docker Setup
Build the Docker Image

docker build -t social-analyzer .

Run the Container

docker run -p 8501:8501 social-analyzer

Access the application at:
http://localhost:8501