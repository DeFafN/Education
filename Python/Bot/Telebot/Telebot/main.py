import telebot
import sqlite3 as DB
import pandas as PD
import datetime as DT
from telebot import types
from config import bot

connection = DB.connect('bot.db')
cursor = connection.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS Messages (
username TEXT,
profile TEXT,
name TEXT,
location TEXT,
salary TEXT,           
work_mode TEXT,    
stack TEXT,
experience TEXT,                
resume TEXT,        
coment TEXT,         
hashtag TEXT,   
date timestamp)
''')
connection.commit()
connection.close()

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
HELP = """ 
/help - помощь
/start - отправить информацию по кандидату

"""
        
@bot.message_handler(commands = ['start', 'help'])
def commands(message):
    if message.text == "/help":
        bot.send_message(message.chat.id, HELP)
    elif message.text == "/start":
        global username
        username = message.from_user.first_name + " " + message.from_user.last_name
        bot.send_message(message.from_user.id, "Укажи профиль кандидата")
        bot.register_next_step_handler(message, get_profile)
    else:
        bot.send_message(message.chat.id, "Напиши /help или /start")

def get_profile(message):
    global profile
    profile = str(message.text)
    bot.send_message(message.from_user.id, 'Напиши фамилию и инициалы кандидата')
    bot.register_next_step_handler(message, get_name)

def get_name(message):
    global name
    name = str(message.text)
    
    bot.send_message(message.from_user.id, 'Из какого города кандидат?')
    bot.register_next_step_handler(message, get_location)

def get_location(message):
    global location
    location = str(message.text)
    bot.send_message(message.from_user.id, 'Какие зарплатные ожидания у кандидата?')
    bot.register_next_step_handler(message, get_salary)

def get_salary(message):
    global salary
    salary = str(message.text)
    bot.send_message(message.from_user.id, 'Какие форматы работы рассматривает кандидат')
    bot.register_next_step_handler(message, get_work_mode)

def get_work_mode(message):
    global work_mode
    work_mode = str(message.text)
    bot.send_message(message.from_user.id, 'Укажи стэк кандидата')
    bot.register_next_step_handler(message, get_stack)

def get_stack(message):
    global stack
    stack = str(message.text)
    bot.send_message(message.from_user.id, 'Укажи ссылку на резюме кандидата')
    bot.register_next_step_handler(message, get_resume)

def get_resume(message):
    global resume
    resume = str(message.text)
    bot.send_message(message.from_user.id, 'комментарий')
    bot.register_next_step_handler(message, get_coment)

def get_coment(message):
    global coment
    coment = str(message.text)
    bot.send_message(message.from_user.id, 'Какой стаж?')
    bot.register_next_step_handler(message, get_experience)

def get_experience(message):
    global experience
    experience = str(message.text)
    bot.send_message(message.from_user.id, 'хештэг?')
    bot.register_next_step_handler(message, get_hashtag)

def get_hashtag(message):
    global hashtag
    hashtag = str(message.text)
    bot.send_message(message.from_user.id, 'проверь всё-ли верно в следующем сообщении, а сейчас напиши что-нибудь')
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
    date = DT.datetime.now()
    connection = DB.connect('bot.db')
    cursor = connection.cursor()
    data = (username, profile, name, location, salary, work_mode, stack, experience, resume, coment, hashtag, date,)
    cursor.execute("""INSERT INTO Messages (username, profile, name, location, salary, work_mode, stack, experience, resume,
    coment, hashtag, date) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""", (data))
    connection.commit()
    connection.close()
    connection = DB.connect('bot.db')
    cursor = connection.cursor()
    temp = cursor.execute("""SELECT * FROM Messages ORDER BY date DESC LIMIT 1""")
    raw = cursor.fetchall()
    candidat = list(zip(*raw))
    connection.close()
    bot.send_message(message.chat.id, f'{*candidat[1:-2],} всё верно? (да/нет)')
    bot.register_next_step_handler(message, aprove)
    
def aprove(message):
    if message.text.lower == "да":
        bot.send_message(chat_id=1737541145, text=f'{*candidat[1:-2],}', allow_sending_without_reply=True)
    else:
        bot.register_next_step_handler(message, commands)


@bot.message_handler(content_types=['text'])
def handle_text(message):
    bot.send_message(message.from_user.id, "Напиши /help")

bot.polling()