import os
from google import genai

# Load API key


def summarize_news(news_items,genai_api_key):
    client = genai.Client(api_key=genai_api_key)
    summaries = []
    for title, desc in news_items:
        prompt = f"Summarize this news headline and description:\nTitle: {title}\nDescription: {desc}"
        response = client.models.generate_content(model='gemini-2.0-flash',contents=prompt)
        summaries.append(response.text.strip())
    return summaries
