from fastapi import FastAPI
import datascrape
import infoprompt
import news
import yfinance as yf
import gptprompt
from pydantic import BaseModel



class Data(BaseModel):
    date_from: str
    date_to: str

app = FastAPI()

@app.get("/{industry}")
async def fetch_data(industry : str, data : Data):

    date_from = data.date_from
    date_to = data.date_to
    
    if not industry or not date_from or not date_to :
        return ({"error": "No data provided"}), 400
    
    top_companies = datascrape.topCompanies(industry)
    updated_companies = list(map(
        lambda company : yf.Ticker(company["code"]).info,
        top_companies
    ))
    
    news_info = news.newsInfo(updated_companies, industry, date_from, date_to)
    news_prompt = infoprompt.newsPrompt(news_info, industry)
    market_prompt = infoprompt.infoPrompt(updated_companies, industry)
    ai_init_answer = gptprompt.aiInitPrompt(news_prompt, market_prompt, industry)

    return ai_init_answer