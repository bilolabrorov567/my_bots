import requests

# USD
# EUR
# RUB
# TRY
# KZT


def get_rates():
    r = requests.get("https://cbu.uz/uz/arkhiv-kursov-valyut/json/")
    our_rates = {}
    data = r.json()
    for rate in data:
        rate_code = rate["Ccy"]
        if rate_code in ["USD", "EUR", "RUB", "TRY", "KZT"]:
            our_rates[rate_code] = rate
    return our_rates

# print(get_rates()["USD"]["Rate"])


# [ [1,2], [3,4], [5,6], [7,8] ]





    
