from bs4 import BeautifulSoup
import requests


def industry_list():
    page = requests.get("https://companiesmarketcap.com/all-categories/")
    soup = BeautifulSoup(page.content, "html.parser")
    body_list = soup.find("tbody")
    table_list = body_list.find_all("td")
    
    def title_search(el) : 
        search = el.find('a')
        if search and search is not None: 
            data = el.get("data-sort")
            href = search.get('href')
            data = data.replace(' ', '-').replace('&', 'and').lower()
            
            return {"name" : data, "href" : href}
        
    result = [title_search(el) for el in table_list if title_search(el) is not None]
        
    return result

def top_companies(url: str):
    
    page = requests.get(f"https://companiesmarketcap.com/{url}")
    soup = BeautifulSoup(page.content, 'html.parser')
    body = soup.find('tbody')
    table_list = body.select("td.name-td")[:5]
    def extract_company(el) : 
        company_name = el.select_one("div.company-name").text.strip()
        company_code = el.select_one("div.company-code").text.strip()
        return {"name" : company_name, "code": company_code}
    
    result = list(map(lambda el: extract_company(el), table_list))
        
    return result

# lambda <arguments> : <Return Value if condition is True> if <condition> else <Return Value if condition is False>