import requests
from datetime import date
import xmltodict

def get_usd_rate():
    today = date.today().strftime("%d/%m/%Y")
    response = requests.get(f"https://www.cbr.ru/scripts/XML_daily.asp?date_req={today}")
    dict_data = xmltodict.parse(response.content)
    usd_rate = [item for item in dict_data['ValCurs']['Valute'] if item['CharCode'] == "USD"]
    return usd_rate[0]