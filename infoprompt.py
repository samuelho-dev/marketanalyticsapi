from datetime import date
import pandas as pd

def infoPrompt(infoList, industry) :
  marketprompt = f'The top {industry} 50 companies have the following information : '
  for idx, company in enumerate(infoList) :
    longName = company["longName"]
    symbol = company["symbol"]
    epsCurrentYear = company["epsCurrentYear"]
    marketCap = company["marketCap"]
    today = date.today()
    prompt = f'#{idx + 1} company, {longName} with the symbol {symbol}, has the following stats as of {today}: Market Cap: {marketCap}, eps: {epsCurrentYear}. '
    marketprompt += prompt
  return marketprompt