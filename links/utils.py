import requests
import json

from fake_useragent import UserAgent


def get_info(product_name):
    """Get info from URL using Selenium"""
    useragent = UserAgent()

    headers = {
        'User-Agent': useragent.opera,
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }

    try:
        r = requests.get(f"https://www.ozon.ru/api/composer-api.bx/page/json/v2?url=%2Fproduct%2F{product_name}", headers=headers)
        
        name = json.loads(r.json().get("widgetStates").get("webCharacteristics-545710-default-1")).get("productTitle")

        result = []
        for i in json.loads(r.json().get("widgetStates").get("webPrice-952422-default-1")).get("price"):
            if i.isnumeric():
                result.append(i)
        price = int("".join(result))

        return name, price

    except Exception as e:
        print(e)

