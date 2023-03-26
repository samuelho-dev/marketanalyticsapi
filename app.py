from flask import Flask
import yfinance as yf

app = Flask(__name__)

@app.route("/")
def hello_world():
    return {"hello" : "world"}

@app.route("/")
def hello_world():
    return {"hello" : "world"}
