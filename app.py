from flask import Flask, render_template, request, url_for, redirect
import json

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    with open("common.json", "r") as f:
        common = json.load(f)
    return render_template("index.html", common = common)

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