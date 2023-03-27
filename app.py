from flask import Flask, jsonify
import datascrape
import infoprompt
import news
import yfinance as yf
import gptprompt

app = Flask(__name__)


@app.route("/")  # /market/<marketid>
def fetchData():
    industry = "real-estate"
    topCompanies = datascrape.topCompanies(industry)
    
    updatedCompanies = []
    for company in topCompanies:
        ticker = yf.Ticker(company["code"])
        updatedCompanies.append(ticker.info)
    
    newsInfo = news.newsInfo(updatedCompanies, industry)
    newsPrompt = infoprompt.newsPrompt(newsInfo, industry)
    marketPrompt = infoprompt.infoPrompt(updatedCompanies, industry)
    aiInitAnswer = gptprompt.aiInitPrompt(newsPrompt, marketPrompt, industry)

    return jsonify({'answer' : aiInitAnswer})



if __name__ == "__main__":
    app.run(debug=True)