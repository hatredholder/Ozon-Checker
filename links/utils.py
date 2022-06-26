import json

import requests
from fake_useragent import UserAgent


def get_info(**kwargs):
    """Get name and price from the API of requested item"""
    
    for _, product_name in kwargs.items():
        
        # Create a random user agent
        useragent = UserAgent()

        headers = {
            'User-Agent': useragent.opera,
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }

        # Connect to the API
        req = requests.Session()

        r = req.get(f"https://www.ozon.ru/api/composer-api.bx/page/json/v2?url=%2Fproduct%2F{product_name}", headers=headers)

        # Get the name
        name = json.loads(
            r.json().get("widgetStates").get("webCharacteristics-545710-default-1")
        ).get("productTitle")

        # Get the price, 
        # turn the price string to a number
        result = []
        for i in json.loads(r.json().get("widgetStates").get("webPrice-952422-default-1")).get("price"):
            if i.isnumeric():
                result.append(i)
        price = int("".join(result))

        return name, price
