###6***
# Дан список словарей, содержащих информацию о сообщении, полученном от пользователя на сервер. 
# Необходимо написать две функции: сравнивающую текст сообщения с командами, доступными в программе, 
# и вторую фунцкию, создающую новый словарь, содержащий информацию о новом сообщении, 
# отправленным программой

# [{"user_id":1, #Начало списка, содержащего 2 словаря, и начало первого словаря, 
# # содержащего информацию о пользователе.
# "user_first_name":"Alexander",# Ключ и значение, содержащее имя пользователя
# "user_last_name":"Cheburanov"#Ключ и значение, содежащее фамилию пользователя
# "is_bot":False}, #Является ли отправитель сообщения ботом 
# #Конец первого словаря в списке
# {"message_id":0,#Начало второго словаря, содержащего информацию о сообщении
# "date":[28,7,2022],#Дата отправления сообщения
# "text":""}#Текст сообщения. В данном примере он пуст. 
# # Для тестового задания текст в сообщение необходимо записывать, используя функцию input()
# ]

"/start"
"/help"
"/hello"
def create_user_info(user_id,first_name,last_name,is_bot = False):
    user_info = {'user_id':user_id, 
    'user_first_name': first_name,
    'user_last_name': last_name,
    'is_bot': is_bot}
    return user_info

def create_message_info(text):
    message = {
        'message_id': message_id,
        'text': text,
        'date': [15,12,22]
    }
    return message


def create_message(from_user,message):
    full_message = []
    full_message.append(from_user)
    full_message.append(message)
    return full_message

message_id = 0

user = create_user_info(1,'Alexander','Cheburanov')
bot = create_user_info(0,'Test','Bot',True)

def get_message():
    global message_id
    message_id +=1
    message_text = input('Введите текст сообщения ')
    message_info = create_message_info(message_text)
    message = create_message(user,message_info)
    return message

def send_message(text):
    global message_id
    message_id +=1   # message_id = message_id+1
    message_info = create_message_info(text)
    message = create_message(bot,message_info)
    print(message)
    print(text)

def message_handler(message):
    message_text = message[1]['text']
    if message_text == '/start':
        send_message('Бот активирован! Введите /help для справки ')
    elif message_text == '/hello':
        name = message[0]['user_first_name']
        last_name =  message[0]['user_last_name']
        send_text = f'Приветствую! {name} {last_name}, рад тебя видеть!'
        send_message(send_text)
        
    elif message_text == '/help':
        send_message('Доступные команды: \n/start\n/hello\n/help')
    else:
        send_message('Вы ввели недопустимую команду! Попробуйте /help')



while True:

    message_handler(get_message())




[{"user_id":1, 
"user_first_name":"Alexander",
"user_last_name":"Cheburanov",
"is_bot":False}
, 
{"message_id":0,
"date":[28,7,2022],
"text":""}
]