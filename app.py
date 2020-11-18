from flask import Flask, render_template, request, url_for, redirect
import json

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    with open ("data.json", "r") as f:
        data = json.load(f)
    return render_template("index.html", data = data)

@app.route("/company/<name>/", methods=["GET"])
def company_data(name):
    with open ("data.json", "r") as f:
        data = json.load(f)[name]
    return render_template("company.html", data = data)

@app.route("/filter/", methods=["GET", "POST"])
def filter():
    if request.method == "GET":
        return render_template("filter.html", companies = {})

    elif request.method == "POST":
        print(request.form)
        if request.form['id'] == '0':
            divident_yield_start = float( request.form['divident-yield-start'] if request.form['divident-yield-start'] != "" else '-inf' )
            divident_yield_end = float(request.form['divident-yield-end'] if request.form['divident-yield-end'] != "" else 'inf')

            payout_ratio_start = float(request.form['payout-ratio-start'] if request.form['payout-ratio-start'] != "" else '-inf')
            payout_ratio_end = float(request.form['payout-ratio-end'] if request.form['payout-ratio-end'] != "" else 'inf' )

            divident_growth_start = float(request.form['divident-growth-start'] if request.form['divident-growth-start'] != "" else '-inf')
            divident_growth_end = float(request.form['divident-growth-end'] if request.form['divident-growth-end'] != "" else 'inf')

            beta_start = float(request.form['beta-start'] if request.form['beta-start'] != "" else '-inf')
            beta_end = float(request.form['beta-end'] if request.form['beta-end'] != "" else 'inf')

            companies = dict()

            with open("data.json", "r") as f:
                data = json.load(f)
            
            for key, value in data.items():
                dy = value['Data']['Dividend Yield ANN'][0].strip("%").replace(",", "")
                pr = value['Data']['Payout Ratio TTM'][0].strip("%").replace(",", "")
                dg = value['Data']['Dividend Growth Rate ANN'][0].strip("%").replace(",", "")
                b = value['Data']['P/E Ratio TTM'][0].strip("%").replace(",", "")

                if (dy == pr == dg == b == '-'):
                    continue

                if  ( dy == '-' or ( float(dy) >=  divident_yield_start and float(dy) <= divident_yield_end) ) and \
                    ( pr == '-' or ( float(pr) >=  payout_ratio_start and float(pr) <= payout_ratio_end) ) and \
                    ( dg == '-' or ( float(dg) >=  divident_growth_start and float(dg) <= divident_growth_end) ) and \
                    ( b == '-' or ( float(b) >=  beta_start and float(b) <= beta_end) ) :

                    companies[key] = value

            return render_template("filter.html", companies = companies, id = 0)

        elif request.form['id'] == '1':
            _5_yr_eps_start = float( request.form['5-yr-eps-start'] if request.form['5-yr-eps-start'] != "" else '-inf' )
            _5_yr_eps_end = float(request.form['5-yr-eps-end'] if request.form['5-yr-eps-end'] != "" else 'inf')

            _5_yr_sales_start = float(request.form['5-yr-sales-start'] if request.form['5-yr-sales-start'] != "" else '-inf')
            _5_yr_sales_end = float(request.form['5-yr-sales-end'] if request.form['5-yr-sales-end'] != "" else 'inf' )

            beta_start = float(request.form['beta-start'] if request.form['beta-start'] != "" else '-inf')
            beta_end = float(request.form['beta-end'] if request.form['beta-end'] != "" else 'inf')

            curr_ratio_start = float(request.form['curr-ratio-start'] if request.form['curr-ratio-start'] != "" else '-inf')
            curr_ratio_end = float(request.form['curr-ratio-end'] if request.form['curr-ratio-end'] != "" else 'inf')

            eps_start = float(request.form['eps-start'] if request.form['eps-start'] != "" else '-inf')
            eps_end = float(request.form['eps-end'] if request.form['eps-end'] != "" else 'inf')

            companies = dict()

            with open("data.json", "r") as f:
                data = json.load(f)
            
            for key, value in data.items():
                ye = value['Data']['5 Year EPS Growth 5YA'][0].strip("%").replace(",", "")
                ys = value['Data']['5 Year Sales Growth 5YA'][0].strip("%").replace(",", "")
                cr = value['Data']['Current Ratio MRQ'][0].strip("%").replace(",", "")
                b = value['Data']['P/E Ratio TTM'][0].strip("%").replace(",", "")
                eps = value['Data']['Basic EPS ANN'][0].strip("%").replace(",", "")

                if (ye == ys == cr == b == '-'):
                    continue

                if  ( ye == '-' or ( float(ye) >=  _5_yr_eps_start and float(ye) <=_5_yr_eps_end) ) and \
                    ( ys == '-' or ( float(ys) >=  _5_yr_sales_start and float(ys) <= _5_yr_sales_end) ) and \
                    ( cr == '-' or ( float(cr) >=  curr_ratio_start and float(cr) <= curr_ratio_end) ) and \
                    ( b == '-' or ( float(b) >=  beta_start and float(b) <= beta_end) ) and \
                    ( eps == '-' or ( float(eps) >=  eps_start and float(eps) <= eps_end) ) :

                    companies[key] = value

            return render_template("filter.html", companies = companies, id = 1)

        return render_template("filter.html", companies = {})

if __name__ == "__main__":
    # create_db()
    app.run(port=5000, debug=True)