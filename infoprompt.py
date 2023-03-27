from datetime import date

def infoPrompt(infoList, industry):
    today = date.today()
    marketprompt = f'This is the top {industry} companies as of {today}. Here are some key stats:\n'
    for idx, company in enumerate(infoList):
        longName = company["longName"]
        symbol = company["symbol"]
        epsCurrentYear = company["epsCurrentYear"]
        marketCap = company["marketCap"]
        prompt = f'{idx + 1}. {longName} ({symbol}): Market Cap: {marketCap}, EPS: {epsCurrentYear}. \n'
        marketprompt += prompt
    return marketprompt


def newsPrompt(articles, industry) :
  
  newsprompt = f'These are the news articles for the {industry} industry companies: \n'
  for article in articles: 
    sourceName = article['sourceName']
    author = article['author']
    title = article['title']
    description = article['description']
    content = article['content']
    prompt = f'This is an article from {sourceName} by {author}, the title is {title}. Here is the short description: {description}. This is the content: {content} \n'
    newsprompt += prompt
  return newsprompt

