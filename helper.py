import requests
from bs4 import BeautifulSoup
import json
from pprint import pprint

def getSoup(link):
    headers = {'User-Agent' : 'PostmanRuntime/7.24.1', 'Accept': "*/*", "Connection": 'keep-alive'}
    req = requests.get(link, headers=headers)
    html = req.content
    soup = BeautifulSoup(html, "html.parser")
    return soup

def get_links(file):
    links = list()
    left = list()

    with open(file, "r") as f:
        tickers = json.load(f)
    for ticker in tickers:
        soup = getSoup(f"https://www.investing.com/search/?q={ticker}")
        try:
            link = soup.find("a", {"class": "js-inner-all-results-quote-item row"})["href"].split("?")[0]
            link = f"https://www.investing.com{link}-ratios"
            links.append(link)
            print(link)
        except:
            left.append(ticker)
            
    with open("left.json", "w") as f:
        json.dump(left, f)
    with open("companies_link.json", "w") as f:
        json.dump(links, f)


def get_ratios(link):
    soup = getSoup(link)
    title = soup.find("title").text.replace(" ", "-")
    table = soup.find("table", {"id": "rrTable"})
    trs = table.findAll("tr", {"class": "child"})
    ratios = dict()
    for tr in trs:
        tds = tr.findAll("td")
        try:
            ratios[tds[0].text] = [tds[1].text, tds[2].text]
        except:
            pass
    print(title)
    return {title:ratios}

def cor():
    with open("data.json", "r") as f:
        data = json.load(f)
    data1 = {}
    for key, value in data.items():
        data1[key.replace(" ", "-")] = value

    with open("data.json", "w") as f:
        json.dump(data1, f)

if __name__ == "__main__":
    cor()