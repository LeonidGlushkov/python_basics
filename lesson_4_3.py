import requests
from datetime import datetime
from decimal import Decimal


def currency_rates(value):
    response = requests.get('https://www.cbr-xml-daily.ru/daily_json.js')
    date = datetime.strptime(response.headers['Date'], '%a, %d %B %Y %H:%M:%S %Z').date()
    response = response.json()
    if not response['Valute'].get(value.upper()):
        return
    return f'{Decimal(str(response["Valute"].get(value.upper())["Value"]))}, {date}'

print(currency_rates('j'))
print(currency_rates('usd'))

