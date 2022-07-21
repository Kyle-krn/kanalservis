import requests
import config
import urllib.parse

def send_chanel_msg(text):
    params = {
        'chat_id': config.CHANEL_ID,
        "text": text
    }
    return requests.get(url=f'https://api.telegram.org/bot{config.BOT_TOKEN}/sendMessage', params=params)
    