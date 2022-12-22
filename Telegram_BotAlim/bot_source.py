import requests
import json
import time
TOKEN = '5683608663:AAFkp0VmPqjzG6X48w8UsxxMJZiaXrEcHEI'
METHOD = ''
bot_url = f'hhtps://api.telegram.org/bot{TOKEN}/{METHOD}'

OFFSET = 0

def get_updates(offset):
    METHOD = f'getUpdates?offset={offset}'
    url = bot_url + METHOD
    tg_request = requests.get(url)
    try:
        tg_data = json.loads(tg_request.text)
        return tg_data
    except Exception as er:
        print(er)

while True:
    time.sleep(2)
    bot_data = get_updates(OFFSET)
    print(bot_data)
    