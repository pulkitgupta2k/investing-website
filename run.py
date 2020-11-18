from helper import *


def ratios_driver():
    with open("companies_link.json", "r") as f:
        companies = json.load(f)
    
    data1 = {}
    for company in companies:
        print(company)
        try:
            data1.update(get_ratios(company))
        except:
            print(f"Error in {company}")

    with open("data.json", "w") as f:
        json.dump(data1, f)

if __name__ == "__main__":
    ratios_driver()
    add_ex()
    add_cat()
