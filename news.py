from newsapi import NewsApiClient
import os

newsapi = NewsApiClient(os.getenv("NEWS_API_KEY"))

def news_info(updatedCompanies, industry, date_from, date_to):
    data = []
    for company in updatedCompanies:
        symbol = company["symbol"]
        name = company["longName"]
        query = f"{industry} industry {symbol} {name}"
        PARAMS = {
            "q": query,
            "from": date_from,
            "to": date_to,
            "page": 2,
            "sortBy": "relevancy",
        }
        request = newsapi.get_everything(PARAMS)
        print(request)
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
