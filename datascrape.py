from bs4 import BeautifulSoup
import requests


def industry_list():
    page = requests.get("https://companiesmarketcap.com/all-categories/")
    soup = BeautifulSoup(page.content, "html.parser")
    list = soup.find("tbody")
    table_list = list.find_all("td")
    
    def title_search(el) : 
        search = el.find('a')
        if search: 
            return el.get("data-sort")
            
    result = list(map(lambda el: title_search(el), table_list))
        
    return result

async def top_companies(industry):
    page = requests.get(f"https://companiesmarketcap.com/{industry}/largest-{industry}-companies-by-market-cap/")
    soup = BeautifulSoup(page.content, 'html.parser')
    list = soup.find('tbody')
    table_list = list.select("td.name-td")[:5]
    
    def extract_company(el) : 
        company_name = el.select_one("div.company-name").text.strip()
        company_code = el.select_one("div.company-code").text.strip()
        return {"name" : company_name, "code": company_code}
    result = list(map(lambda el: extract_company(el), table_list))
        
    return result

