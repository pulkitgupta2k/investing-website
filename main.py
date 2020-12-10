from flask import Flask, render_template, request, url_for, redirect
import json
from pprint import pprint

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/stock-screener", methods=["GET", "POST"])
def stock_screener():
    if request.method == "GET":
        with open("common.json", "r") as f:
            common = json.load(f)
        return render_template("stock-screener.html", common=common)
    if request.method == "POST":
        with open("common.json", "r") as f:
            common = json.load(f)

        location = request.form.getlist("location")
        category = request.form.getlist("category")

        ret_common = {}
        for key, value in common.items():
            if value["location"] in location and value["category"] in category and \
                    float(request.form["de_ratio_begin"]) <= float(value["ratios"]["de_ratio"] or 0) <= float(request.form["de_ratio_end"]) and \
                    float(request.form["eps_begin"]) <= float(value["ratios"]["eps"] or 0) <= float(request.form["eps_end"]) and \
                    float(request.form["ret_eq_begin"]) <= float(value["ratios"]["ret_eq"] or 0) <= float(request.form["ret_eq_end"]) and \
                    float(request.form["q_ratio_begin"]) <= float(value["ratios"]["q_ratio"] or 0) <= float(request.form["q_ratio_end"]) and \
                    float(request.form["div_y_begin"]) <= float(value["ratios"]["div_y"] or 0) <= float(request.form["div_y_end"]) and \
                    float(request.form["op_pro_begin"]) <= float(value["ratios"]["op_pro"] or 0) <= float(request.form["op_pro_end"]) and \
                    float(request.form["int_cov_begin"]) <= float(value["ratios"]["int_cov"] or 0) <= float(request.form["int_cov_end"]) and \
                    float(request.form["div_pay_begin"]) <= float(value["ratios"]["div_pay"] or 0) <= float(request.form["div_pay_end"]) and \
                    float(request.form["ret_cap_begin"]) <= float(value["ratios"]["ret_cap"] or 0) <= float(request.form["ret_cap_end"]):
                ret_common[key] = value

        return render_template("stock-screener.html", common=ret_common)


@app.route("/graph", methods=["GET", "POST"])
def graph():

    with open("common.json", "r") as f:
        common = json.load(f)
    if request.method == "GET":
        return render_template("graph.html", common=common, selected={}, data=[[]])
    if request.method == "POST":
        selected = {}
        data = [[] for x in range(10)]
        for ticker in request.form['values'].split(','):
            selected[ticker] = common[ticker]
            data[0].append(ticker)
            data[1].append(selected[ticker]['ratios']['de_ratio'] or 0)
            data[2].append(selected[ticker]['ratios']['eps'] or 0)
            data[3].append(selected[ticker]['ratios']['ret_eq'] or 0)
            data[4].append(selected[ticker]['ratios']['q_ratio'] or 0)
            data[5].append(selected[ticker]['ratios']['div_y'] or 0)
            data[6].append(selected[ticker]['ratios']['op_pro'] or 0)
            data[7].append(selected[ticker]['ratios']['int_cov'] or 0)
            data[8].append(selected[ticker]['ratios']['div_pay'] or 0)
            data[9].append(selected[ticker]['ratios']['ret_cap'] or 0)

        return render_template("graph.html", common=common, selected=selected, data=data)


@app.route("/rank")
def rank():
    with open("common.json", "r") as f:
        common = json.load(f)
    data = {}

    country_score = {
        "B3 S.A. - Brasil, Bolsa, Balc\u00c3\u00a3o": 108.5,
        "Hong Kong Exchanges And Clearing Ltd": 135.5,
        "New York Stock Exchange, Inc.": 155.5,
        "Nasdaq": 155.5,
        "London Stock Exchange": 110.5,
        "Toronto Stock Exchange": 143,
        "Shanghai Stock Exchange": 136,
        "Shenzhen Stock Exchange": 136,
        "BSE LTD": 138.5
    }

    for key, value in common.items():
        if value['category'] == 'ENERGY' or value['category'] == 'PRODUCER DURABLES' or value['category'] == 'OTHERS' or \
            value['industry'] not in {"Personal care", "Pharmaceuticals", "Diversified retail", "Financial data & systems", "Computer technology",  \
               "Utilities: Miscellaneous", "Computer services software and systems" , "Diversified financial services"}:
            continue
        score = 0
        score += (value['ratios']['ret_cap'] or 0)\
            + 10*(value['ratios']['q_ratio'] or 0) \
            - (abs(value['ratios']['de_ratio'] or 0)) \
            + 10*(value['ratios']['op_pro'] or 0) \
            + (value['ratios']['ret_eq'] or 0) \
            + country_score[value['location']]

        value['score'] = int(score)
        if value['industry'] not in data.keys():
            data[value['industry']] = []
        data[value['industry']].append(value)

    for key, value in data.items():
        data[key] = sorted(data[key], key=lambda k: k['score'], reverse=True)
    return render_template("rank.html", data=data)


@app.route("/company/<ticker>/", methods=["GET"])
def company(ticker):
    with open(f"data/{ticker}.json") as f:
        data = json.load(f)
    return render_template("company.html", data=data)


@app.route("/financial/<ticker>/", methods=["GET"])
def financials(ticker):
    with open(f"data/{ticker}.json") as f:
        data = json.load(f)
    return render_template("financials.html", data=data)


@app.route("/module/<num>/", methods=["GET"])
def module(num):
    return render_template(f"modules/{num}.html")


@app.route("/test/<num>/", methods=["GET", "POST"])
def test(num):
    if request.method == "GET":
        with open(f"questions/{num}.json", "r") as f:
            data = json.load(f)
        return render_template(f"test.html", data=data, num=num)
    if request.method == "POST":
        choices = dict(request.form)
        with open(f"questions/{num}.json", "r") as f:
            data = json.load(f)

        score = 0
        for q, a in choices.items():
            if data[int(q)]['ans'] == int(a):
                score += 1

        return render_template(f"test_ans.html", data=data, num=num, choices=choices, score=score)


@app.route("/loaderio-96afe2fea8314b6f56d9537de31c33a3/")
def testing():
    return "loaderio-96afe2fea8314b6f56d9537de31c33a3"


if __name__ == "__main__":
    app.run(debug=True)
