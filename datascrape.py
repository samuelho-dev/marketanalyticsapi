from bs4 import BeautifulSoup
import requests


def industryList():
    page = requests.get("https://companiesmarketcap.com/all-categories/")
    soup = BeautifulSoup(page.content, "html.parser")
    list = soup.find("tbody")
    tableList = list.find_all("td")
    
    industryList = []
    for el in tableList:
        titleSearch = el.find('a')
        if titleSearch: 
            industry = el.get("data-sort")
            industryList.append(industry)
    return industryList

def topCompanies(industry):
    page = requests.get(f"https://companiesmarketcap.com/{industry}/largest-{industry}-companies-by-market-cap/")
    soup = BeautifulSoup(page.content, 'html.parser')
    list = soup.find('tbody')
    tableList = list.select("td.name-td")[:5]
    companyList = []
    for td in tableList:
        companyName = td.select_one("div.company-name").text.strip()
        companyCode = td.select_one("div.company-code").text.strip()
        companyList.append({"name" : companyName, "code": companyCode})
    return companyList

