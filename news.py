import requests
from dotenv import load_dotenv
import os


def newsInfo(updatedCompanies, industry, date_from, date_to):
    data = []
    API_KEY = os.getenv("NEWS_API_KEY")
    
    for company in updatedCompanies:
        symbol = company["symbol"]
        name = company["longName"]
        query = f"{industry} industry {symbol} {name}"
        URL = f"https://newsapi.org/v2/everything"
        PARAMS = {
            "q": query,
            "from": date_from,
            "to": date_to,
            "pageSize": 2,
            "sortBy": "relevancy",
            "apiKey": API_KEY,
        }
        request = requests.get(url=URL, params=PARAMS)
        articles = request.json()["articles"]
        results = request.json()["totalResults"]
        if results > 0:
            for article in articles:
                obj = {
                    "sourceName": article["source"]["name"],
                    "author": article["author"],
                    "title": article["title"],
                    "description": article["description"],
                    "content": article["content"],
                    "publishedAt": article["publishedAt"]
                }
                data.append(obj)

    return data
