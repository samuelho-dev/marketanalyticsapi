from flask import Flask, jsonify
import datascrape
import infoprompt
import yfinance as yf

app = Flask(__name__)


@app.route("/")  # /market/<marketid>
def fetchData():
    topCompanies = datascrape.topCompanies("real-estate")
    
    updatedCompanies = []
    for company in topCompanies:
        ticker = yf.Ticker(company["code"])
        companyData = {"name": company["name"], "code": company["code"], "data": ticker.info}
        updatedCompanies.append(companyData)
    
    infoprompt.infoPrompt(updatedCompanies)
    
    return jsonify(updatedCompanies)



if __name__ == "__main__":
    app.run(debug=True)


