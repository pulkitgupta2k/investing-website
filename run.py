from helper import *


def ratios_driver():
    with open("companies_link.json", "r") as f:
        companies = json.load(f)
    with open("data.json", "r") as f:
        data = json.load(f)

    for company in companies:
        try:
            data.update(get_ratios(company))
        except:
            print(f"Error in {company}")

    with open("data.json", "w") as f:
        json.dump(data, f)

if __name__ == "__main__":
    ratios_driver()