from flask import Flask, render_template, request, url_for, redirect
import json

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    with open ("data.json", "r") as f:
        companies = json.load(f).keys()
    print(companies)
    return render_template("index.html", companies = companies)

@app.route("/company/<name>/", methods=["GET"])
def company_data(name):
    with open ("data.json", "r") as f:
        data = json.load(f)[name]
    return render_template("company.html", data = data)



if __name__ == "__main__":
    # create_db()
    app.run(port=5000, debug=True)