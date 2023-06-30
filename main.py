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

@app.get('/')
def fetch_industries():
    return datascrape.industry_list()

@app.get("/industry/{industry}")
def fetch_data(industry : str, url: str, date_from : str, date_to : str):
    
    if not industry or not date_from or not date_to :
        return {"error": "No data provided"}, 400
    
    top_companies = datascrape.top_companies(url)

    updated_companies = []
    for company in top_companies:
        try:
            info = yf.Ticker(company["code"]).info
            updated_companies.append(info)
        except Exception as e:
            print(f"Error getting info for company {company['code']}: {e}")

    news_info = news.news_info(updated_companies, industry, date_from, date_to)
    news_prompt = infoprompt.news_prompt(news_info, industry)
    market_prompt = infoprompt.info_prompt(updated_companies, industry)
    ai_init_answer = gptprompt.ai_init_prompt(news_prompt, market_prompt, industry)

    return ai_init_answer
