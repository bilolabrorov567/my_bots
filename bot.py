
import requests

def well(exchange):
    try:
        r = requests.get(f"https://www.freeforexapi.com/api/live?pairs={exchange}")
        response = r.json()
        rate = response["rates"][exchange]["rate"]
        return  f"{exchange} well {rate}"

    except:
        print("Sorry, we couldn't find the information")