import requests

def fetch_news(ticker, api_key):
    url = f"https://newsapi.org/v2/everything?q={ticker}&sortBy=publishedAt&apiKey={api_key}"
    response = requests.get(url)
    articles = response.json()["articles"][:5]
    return [(a["title"], a["description"]) for a in articles]
