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
        return render_template("stock-screener.html", common = common)
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
                float(request.form["div_pay_begin"]) <= float(value["ratios"]["div_pay"] or 0) <= float(request.form["div_pay_end"]) :
                ret_common[key] = value

        return render_template("stock-screener.html", common = ret_common)

@app.route("/company/<ticker>/", methods=["GET"])
def company(ticker):
    with open(f"data/{ticker}.json") as f:
        data = json.load(f)
    return render_template("company.html", data = data)

@app.route("/financial/<ticker>/", methods=["GET"])
def financials(ticker):
    with open(f"data/{ticker}.json") as f:
        data = json.load(f)
    return render_template("financials.html", data = data)

@app.route("/module/<num>/", methods=["GET"])
def module(num):
    return render_template(f"modules/{num}.html")

@app.route("/test/<num>/", methods=["GET", "POST"])
def test(num):
    if request.method == "GET":
        with open(f"questions/{num}.json", "r") as f:
            data = json.load(f)
        return render_template(f"test.html", data = data, num=num)
    if request.method == "POST":
        choices = dict(request.form)
        with open(f"questions/{num}.json", "r") as f:
            data = json.load(f)
        return render_template(f"test_ans.html", data = data, num=num, choices = choices)

if __name__ == "__main__":
    app.run(debug=True)