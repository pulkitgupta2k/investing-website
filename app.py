from flask import Flask, render_template, request, url_for, redirect
import json
from pprint import pprint

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        with open("common.json", "r") as f:
            common = json.load(f)
        return render_template("index.html", common = common)
    if request.method == "POST":
        with open("common.json", "r") as f:
            common = json.load(f)

        location = request.form.getlist("location")
        category = request.form.getlist("category")

        ret_common = {}

        for key, value in common.items():
            if value["location"] in location and value["category"] in category:
                ret_common[key] = value

        return render_template("index.html", common = ret_common)


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

if __name__ == "__main__":
    app.run(debug=True)