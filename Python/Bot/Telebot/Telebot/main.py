import telebot
import sqlite3 as DB
import datetime as DT
from telebot import types
from config import bot

username = '*'
profile = '*'
name  = '*'
location = '*'
salary = '*'
work_mode = '*'
stack = '*'
experience = '*'
resume = '*'
coment = '*'
hashtag = '*'
date = '*'
candidat = "*"
boxes = ['Профиль', 'Фамилия и инициалы', 'Локация', 'Стаж работы профильный', 'З/П ожидания', 'Режим работы', 'Стэк технологий',
         'Комментарий от рекрутера', 'Резюме', 'Хэштеги']
result_list = []
result_message = ''

connection = DB.connect('bot.db')
cursor = connection.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS Messages (
profile TEXT,
name TEXT,
location TEXT,
experience TEXT,
salary TEXT,
work_mode TEXT,
stack TEXT,
coment TEXT,         
resume TEXT,
hashtag TEXT,
username TEXT,
date timestamp)
''')
connection.commit()
connection.close()
       
@bot.message_handler(commands = ['start'])
def start_command(message):
    global username
    username = message.from_user.first_name + " " + message.from_user.last_name + " " + message.from_user.username
    bot.send_message(message.from_user.id, "Укажи профиль кандидата")
    bot.register_next_step_handler(message, get_profile)

@bot.message_handler(commands = ['stop'])
def stop_command(message):    
    bot.send_message(message.from_user.id, "Устал работать, если что напиши /start")
    
@bot.message_handler(commands = ['help'])
def help_command(message):    
    bot.send_message(message.from_user.id, """
/help - помощь
/start - отправить информацию по кандидату
/stop - прекратить скрипт по передаче кандидата
по вопросам работы бота писать @arpanov""")



def get_profile(message):
    global profile
    if message.text == '/stop':
        bot.send_message(message.from_user.id, "Ну нет так нет")
    else:
        profile = str(message.text)
        bot.send_message(message.from_user.id, 'Напиши фамилию и инициалы кандидата')
        bot.register_next_step_handler(message, get_name)

def get_name(message):
    global name
    if message.text == '/stop':
        bot.send_message(message.from_user.id, "Ну нет так нет")
    else:
        name = str(message.text)
        bot.send_message(message.from_user.id, 'Из какого города кандидат?')
        bot.register_next_step_handler(message, get_location)

def get_location(message):
    global location
    if message.text == '/stop':
        bot.send_message(message.from_user.id, "Ну нет так нет")
    else:
        location = str(message.text)
        bot.send_message(message.from_user.id, 'Какой у кандидата профильный опыт работы?')
        bot.register_next_step_handler(message, get_experience)

def get_experience(message):
    global experience
    if message.text == '/stop':
        bot.send_message(message.from_user.id, "Ну нет так нет")
    else:
        experience = str(message.text)
        bot.send_message(message.from_user.id, 'Какие зарплатные ожидания у кандидата?')
        bot.register_next_step_handler(message, get_salary)
    
def get_salary(message):
    global salary
    if message.text == '/stop':
        bot.send_message(message.from_user.id, "Ну нет так нет")
    else:
        salary = str(message.text)
        bot.send_message(message.from_user.id, 'Какие форматы работы рассматривает кандидат')
        bot.register_next_step_handler(message, get_work_mode)

def get_work_mode(message):
    global work_mode
    if message.text == '/stop':
        bot.send_message(message.from_user.id, "Ну нет так нет")
    else:
        work_mode = str(message.text)
        bot.send_message(message.from_user.id, 'Укажи стэк кандидата')
        bot.register_next_step_handler(message, get_stack)

def get_stack(message):
    global stack
    if message.text == '/stop':
        bot.send_message(message.from_user.id, "Ну нет так нет")
    else:
        stack = str(message.text)
        bot.send_message(message.from_user.id, 'Твои комментарии')
        bot.register_next_step_handler(message, get_coment)

def get_coment(message):
    global coment
    if message.text == '/stop':
        bot.send_message(message.from_user.id, "Ну нет так нет")
    else:
        coment = str(message.text)
        bot.send_message(message.from_user.id, 'Вставь ссылку на резюме')
        bot.register_next_step_handler(message, get_resume)

def get_resume(message):
    global resume
    if message.text == '/stop':
        bot.send_message(message.from_user.id, "Ну нет так нет")
    else:
        resume = str(message.text)
        bot.send_message(message.from_user.id, 'Напиши хэштеги')
        bot.register_next_step_handler(message, get_hashtag)

def get_hashtag(message):
    global hashtag
    if message.text == '/stop':
        bot.send_message(message.from_user.id, "Ну нет так нет")
    else:
        hashtag = str(message.text)
        count = 0
        for symbol in hashtag:
            if symbol == '#':
                count +=1
        
        if count < 4:
            bot.send_message(message.from_user.id, 'Проставлены не все тэги')
            bot.register_next_step_handler(message, get_hashtag)
        elif count > 4:
            bot.send_message(message.from_user.id, 'Перебор с тэгами')
            bot.register_next_step_handler(message, get_hashtag)
        else:
            bot.send_message(message.from_user.id, 'Проверь всё-ли верно в следующем сообщении, а сейчас напиши что-нибудь')
            bot.register_next_step_handler(message, check)

def check (message):
    global username
    global profile
    global name
    global location
    global salary
    global work_mode
    global stack
    global experience
    global resume
    global coment
    global hashtag
    global date
    global connection
    global cursor
    global candidat
    global boxes
    global result_list
    global result_message
    if message.text == '/stop':
        bot.send_message(message.from_user.id, "Ну нет так нет")
    else: 
        date = DT.datetime.now()
        connection = DB.connect('bot.db')
        cursor = connection.cursor()
        data = (username, profile, name, location, salary, work_mode, stack, experience, resume, coment, hashtag, date,)
        cursor.execute("""INSERT INTO Messages (username, profile, name, location, salary, work_mode, stack, experience, resume, coment, hashtag, date)
                       VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""", (data))
        connection.commit()
        cursor.execute("""SELECT * FROM Messages ORDER BY date DESC LIMIT 1""")
        raw =  cursor.fetchmany(1)
        candidat = list(zip(*raw))
        connection.close()
        new_kandidat = candidat[0:-2]
        for field, values in zip(boxes, new_kandidat):
            values_str = ', '.join(values)
            result_str = f'{field}: {values_str}'
            result_list.append(result_str)

        result_message = '\n'.join(result_list)
        bot.send_message(message.from_user.id, f'{result_message},\n \n Если всё верно напиши да, если есть ошибки напиши нет')
        bot.register_next_step_handler(message, aprove)
        result_list = []
        

def aprove(message):
    aprove_text = str(message.text.lower())
    
    if aprove_text == "да":
        bot.send_message(chat_id=1315896344, text=f'{result_message}')
        bot.send_message(message.from_user.id, 'Кандидат направлен модератору')
    elif aprove_text == "нет":
        bot.send_message(message.from_user.id, 'Ну нет так нет, придётся начать сначала')
        bot.register_next_step_handler(message, start_command)
    else:
        bot.send_message(message.from_user.id, 'Напиши да или нет')
        bot.register_next_step_handler(message, aprove_text)

@bot.message_handler(content_types=['text'])
def handle_text(message):
    if message.text == '/help':
        bot.register_next_step_handler(message, help_command)    
    elif message.text == '/start':
        bot.register_next_step_handler(message, start_command)    
    elif message.text == '/stop':
        bot.register_next_step_handler(message, stop_command)
    else: 
        bot.send_message(message.from_user.id, "Напиши /help")

bot.polling(none_stop=True)