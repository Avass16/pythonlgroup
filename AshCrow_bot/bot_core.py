import requests
import json
import time

token_file = open('AshCrow_bot/token.txt','rt')

TOKEN = token_file.read()

token_file.close()

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
        
def send_message(chat_id,message_text):
    user_data = {
        'chat_id':chat_id,
        'text':message_text
    }
    try:
        url = BOT_URL+'sendMessage'
        requests.post(url,data = user_data)

    except Exception as er:
        print(er)


def parse_data(data):
    if data['result']:
        offset = data['result'][0]['update_id'] + 1
        message = data['result'][0]['message']
        return offset, message
    else:
        return None,None

def text_handler(message):
    text = message['text']
    chat_id = message['chat']['id']

    if text == '/start':
        send_message(chat_id, 'Привет!')
    elif text =='/help':
         
        pass
    elif text =='/hello':
        pass
    else:
        pass


while True:
    time.sleep(2)

    bot_data = get_updates(OFFSET)    
    OFFSET, message = parse_data(bot_data)
    if message:
        text_handler(message)


