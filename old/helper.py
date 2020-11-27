import requests
from bs4 import BeautifulSoup
import json
from pprint import pprint
import re

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
    ret_dic = {}
    link = link+"-ratios"
    soup = getSoup(link)
    title = soup.find("title").text.replace(" ", "-")
    l = re.split("[()]", title)
    ret_dic[l[1]] = {}
    ret_dic[l[1]]["Name"] = l[0].strip("-")
    table = soup.find("table", {"id": "rrTable"})
    trs = table.findAll("tr", {"class": "child"})
    ratios = dict()
    for tr in trs:
        tds = tr.findAll("td")
        try:
            ratios[tds[0].text] = [tds[1].text, tds[2].text]
        except:
            pass
    ret_dic[l[1]]['Data'] = ratios
    ret_dic[l[1]]['Link'] = link.strip("-ratios")
    return ret_dic

def add_ex():
    with open("data.json", "r") as f:
        data = json.load(f)
    
    with open("loc.json", "r") as f:
        location = json.load(f)
    
    for key in data.keys():
        try:
            data[key]["Exchange"] = location[key][0]["EXCHANGE"]
        except:
            data[key]["Exchange"] = ""
            pass
    
    with open("data.json", "w") as f:
        json.dump(data, f)

def add_cat():
    with open("data.json", "r") as f:
        data = json.load(f)
    
    with open("cat.json", "r") as f:
        cat = json.load(f)
    
    for key, values in cat.items():
        for value in values:
            if value in data.keys():
                data[value]["Category"] = key
                # pprint(data[value])

    for key, value in data.items():
        if "Category" not in value.keys():
            data[key]["Category"] = ""

    with open("data.json", "w") as f:
        json.dump(data, f)


def corr():
    with open("data.json") as f:
        data = json.load(f)
    
    data_new = {}

    for key, value in data.items():
        data_new[key] = {}
        data_new[key]["link"] = value["Link"]
    
    with open("link.json", "w") as f:
        json.dump(data_new, f)

if __name__ == "__main__":
    corr()