import requests
from dotenv import load_dotenv
import os


def newsInfo(updatedCompanies, industry):
    data = []
    API_KEY = os.getenv("NEWS_API_KEY")
    dateRangeFrom = "2022-01-30"
    dateRangeTo = "2023-01-10"
    for company in updatedCompanies:
        symbol = company["symbol"]
        name = company["longName"]
        query = f"{industry} industry {symbol} {name}"
        URL = f"https://newsapi.org/v2/everything"
        PARAMS = {
            "q": query,
            # "from": dateRangeFrom,
            # "to": dateRangeTo,
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
                }
                print(obj)
                data.append(obj)

    return data
