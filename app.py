from flask import Flask, jsonify
import datascrape
import infoprompt
import news
import yfinance as yf

app = Flask(__name__)


@app.route("/")  # /market/<marketid>
def fetchData():
    industry = "real-estate"
    topCompanies = datascrape.topCompanies(industry)
    
    updatedCompanies = []
    for company in topCompanies:
        ticker = yf.Ticker(company["code"])
        updatedCompanies.append(ticker.info)
    
    intitialMarketPrompt = infoprompt.infoPrompt(updatedCompanies, industry)
    newsInfo = news.newsInfo(updatedCompanies, industry)
    return jsonify(updatedCompanies)



if __name__ == "__main__":
    app.run(debug=True)


