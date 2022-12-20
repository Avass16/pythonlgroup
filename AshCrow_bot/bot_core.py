import requests
import json
import time

TOKEN = '5526314084:AAGL5LqSz14D0urgu23ykxoSzWYFkAvaNI8'

METHOD = ''

BOT_URL = f'https://api.telegram.org/bot{TOKEN}/'

OFFSET = 0

def get_updates(offset):
    METHOD = f'getUpdates?offset={offset}'
    url = BOT_URL + METHOD
    
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

