import requests
import json
import glob


def get_json(url, querystring):
    headers = {
        'x-rapidapi-key': "cdf396ea16mshe7d6aa9277936dap1a1da5jsnb264cf0552d7",
        'x-rapidapi-host': "apidojo-yahoo-finance-v1.p.rapidapi.com"
    }
    response = requests.request(
        "GET", url, headers=headers, params=querystring).json()
    return response


def get_summary(ticker):
    url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/v2/get-summary"
    querystring = {"symbol": ticker}
    response = get_json(url, querystring)

    return response


def get_financial(ticker):
    url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/v2/get-financials"
    querystring = {"symbol": ticker}
    response = get_json(url, querystring)
    return response


def get_data(key, value):
    ticker = value['ytick']
    data = get_financial(ticker)
    data.update(get_summary(ticker))

    with open("template.json") as f:
        new_data = json.load(f)

    for key_0, value_0 in new_data.items():
        if value_0 == "":
            new_data[key_0] = data[key_0]
        else:
            for key_1 in new_data[key_0].keys():
                try:
                    new_data[key_0][key_1] = data[key_0][key_1]
                except:
                    pass

    with open(f"data/{key}.json", "w") as f:
        json.dump(new_data, f)


def master_func():
    with open("common.json") as f:
        tickers = json.load(f)

    for file in glob.glob("data/*.json"):
        tickers.pop(file[5:-5])

    left = []
    for key, value in tickers.items():
        try:
            get_data(key,value)
            print(value['ytick'])
        except:
            left.append({key: value})
            print(f"ERROR in {value['ytick']}")


    with open("left.json", "w") as f:
        json.dump(left, f)

def correction():
    # files = []
    # for file in glob.glob("data/*.json"):
    #     files.append(f"data/{file[5:]}")
    
    # for file in files:
    #     with open(file, "r") as f:
    #         data = json.load(f)
    #     data["symbol"] = file[5:-5]
    #     with open(file, "w") as f:
    #         json.dump(data,f)

    # with open("left_new.json") as f:
    #     left = json.load(f)
    # new = {}
    # for row in left:
    #     new[row[1]] = {}
    #     new[row[1]]["name"] = row[0]
    #     if row[2]:
    #         new[row[1]]["ytick"] = row[2].replace(" ", "").upper()
    #     else:
    #         new[row[1]]["ytick"] = row[1]
    #     new[row[1]]["location"] = row[3]
    
    # with open("common.json", "w") as f:
    #     json.dump(new, f)

    ################

    # with open("old/cat.json") as f:
    #     cat = json.load(f)

    # with open("common.json") as f:
    #     common = json.load(f)
    
    # for key, value in cat.items():
    #     for tick in value:
    #         try:
    #             common[tick]["category"] = key
    #         except:
    #             print(tick)
    
    # for key, value in common.items():
    #     if "category" not in value.keys():
    #         print(key)
    #         common[key]["category"] = "OTHERS"

    # with open("common.json", "w") as f:
    #     json.dump(common, f)
    #######################

    # with open("common.json") as f:
    #     common = json.load(f)
    
    # loc = []

    # for key, value in common.items():
    #     if value["category"] not in loc:
    #         loc.append(value["category"])
    #         print(value["category"])
    #######################

    with open("left.json") as f:
        left = json.load(f)
    
    with open("common.json") as f:
        common = json.load(f)
    
    for key, value in left.items():
        common[key] = value
    
    with open("common_new.json", "w") as f:
        json.dump(common,f)

if __name__ == "__main__":
    master_func()
    # correction()
