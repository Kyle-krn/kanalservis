import requests
from datetime import date
import xmltodict
from tg_notification import send_chanel_msg

def get_usd_rate():
    today = date.today().strftime("%d/%m/%Y")
    response = requests.get(f"https://www.cbr.ru/scripts/XML_daily.asp?date_req={today}")
    if response.status_code != 200:
        send_chanel_msg("ЦБ РФ недоступен.")
        return None
    dict_data = xmltodict.parse(response.content)
    usd_rate = [item for item in dict_data['ValCurs']['Valute'] if item['CharCode'] == "USD"]
    if len(usd_rate) == 0:
        send_chanel_msg("USD в ЦБ РФ не найден.")
        return None
    usd_rate = usd_rate[0]['Value']
    if isinstance(usd_rate, float):
        return usd_rate
    elif isinstance(usd_rate, str):
        usd_rate = usd_rate.replace(",", ".")
        usd_rate = float(usd_rate)
        return usd_rate
    return None


if __name__ == "__main__":
    print(get_usd_rate())