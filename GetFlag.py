import requests
import json


def GetFlagImageURL(country):
    url = f'https://restcountries.com/v3.1/name/{country}'

    response = requests.get(url)

    # Проверяем, что запрос прошел успешно
    if response.status_code == 200:
        flag_url = json.loads(response.text)[0]['flags']['png']
        return flag_url
    else:
        print(f'МЭЙДЭЙ МЭЙДЭЙ {country}')