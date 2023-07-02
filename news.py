from newsapi import NewsApiClient
from dotenv import load_dotenv
import os

load_dotenv()

newsapi = NewsApiClient(os.getenv("NEWS_API_KEY"))

def news_info(updatedCompanies, industry, date_from, date_to):
    data = []
    for company in updatedCompanies:
        symbol = company["symbol"]
        name = company["longName"]
        query = f"{industry} industry {symbol} {name}"
        PARAMS = {
            "q": query,
            "from_param": date_from,
            "to": date_to,
            "page": 2,
            "sort_by": "relevancy",
        }
        request = newsapi.get_everything(**PARAMS)
        
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
