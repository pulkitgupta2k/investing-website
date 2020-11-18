from flask import Flask, render_template, request, url_for, redirect
import json

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    with open ("data.json", "r") as f:
        companies = json.load(f).keys()
    return render_template("index.html", companies = companies)

@app.route("/company/<name>/", methods=["GET"])
def company_data(name):
    with open ("data.json", "r") as f:
        data = json.load(f)[name]
    return render_template("company.html", data = data)

@app.route("/pe-ratio/", methods=["GET", "POST"])
def pe_ratio():
    if request.method == "GET":
        return render_template("pe-ratio.html", companies = {})

    elif request.method == "POST":
        start = float(request.form['start'])
        end = float(request.form['end'])

        with open("data.json", "r") as f:
            data = json.load(f)
        
        companies = dict()

        for key, value in data.items():
            try:
                if (value["P/E Ratio TTM"][0] == '-' or float(value["P/E Ratio TTM"][0].replace(",", "")) >= start) and \
                    (value["P/E Ratio TTM"][1] == '-' or float(value["P/E Ratio TTM"][1].replace(",", "")) <= end):
                    companies[key] = value["P/E Ratio TTM"]
            except Exception as e:
                print(e)
                pass

        return render_template("pe-ratio.html", companies = companies)

if __name__ == "__main__":
    # create_db()
    app.run(port=5000, debug=True)