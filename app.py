from flask import Flask, jsonify
import datascrape
import infoprompt
import news
import yfinance as yf
import gptprompt
import requests

app = Flask(__name__)


@app.route("/market/<marketid>", methods=["POST"])
def fetchData(marketid, date_from, date_to):
    industry = marketid
    topCompanies = datascrape.topCompanies(industry)

    updatedCompanies = []
    for company in topCompanies:
        ticker = yf.Ticker(company["code"])
        updatedCompanies.append(ticker.info)

    newsInfo = news.newsInfo(updatedCompanies, industry, date_from, date_to)
    newsPrompt = infoprompt.newsPrompt(newsInfo, industry)
    marketPrompt = infoprompt.infoPrompt(updatedCompanies, industry)
    aiInitAnswer = gptprompt.aiInitPrompt(newsPrompt, marketPrompt, industry)

    return jsonify({"answer": aiInitAnswer})


@app.route("/market/<marketid>", methods=["POST"])
def chat(marketid):
    prompt = requests.json()
    answer = gptprompt.continuePrompt(prompt)
    return jsonify({"answer": answer})


if __name__ == "__main__":
    app.run(debug=True)
