import streamlit as st
from agents.news_fetcher import fetch_news
from agents.sentiment_agent import analyze_sentiment
from agents.summarizer import summarize_news

st.title("Finance Investment Insights Agent")

ticker = st.text_input("Enter Stock Ticker (e.g., AAPL):")

if st.button("Analyze"):
    news = fetch_news(ticker, api_key="a2baa0a6583840ec8a4f95a7184a1c9e")
    summaries = summarize_news(news, genai_api_key="AIzaSyDdIeTB-jZh54irFmYcofRAc8Zg0WEqqnI")

    for i, (summary, (title, _)) in enumerate(zip(summaries, news)):
        sentiment = analyze_sentiment(summary)
        st.subheader(f"News {i+1}: {title}")
        st.write(summary)
        st.markdown(f"**Sentiment**: `{sentiment}`")
