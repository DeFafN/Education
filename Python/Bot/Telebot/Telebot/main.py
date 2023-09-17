import telebot
from telebot import types
from config import bot


PROFILE = '' 
name = ''
location = '' 
salary = ''
work_mode = '' 
stack = '' 
resume = '' 
coment = '' 
hashtag = ''
CANDIDAT = PROFILE + name + location + salary + work_mode + stack + resume + coment + hashtag
# user_data = {profile : '', name : '', location : '', salary : '', work_mode : '', stack : '', resume: '', coment : '', hashtag : ''}

HELP = """ 
/help - помощь
/start - отправить информацию по кандидату

"""

@bot.message_handler(commands = ['start', 'help'])
def commands(message):
    if message.text == "/help":
        bot.send_message(message.chat.id, HELP)
    elif message.text == "/start":
        bot.send_message(message.from_user.id, "Укажи профиль кандидата")
        bot.register_next_step_handler(message, get_profile)
    else:
        bot.send_message(message.chat.id, "Напиши /help или /start")

def get_profile(message):
    profile = message.text
    bot.send_message(message.from_user.id, 'Напиши фамилию и инициалы кандидата')
    global PROFILE
    PROFILE = profile
    bot.register_next_step_handler(message, check)
print(PROFILE)
# def get_name(message):
#     global name
#     name = message.text
#     bot.send_message(message.from_user.id, 'Из какого города кандидат?')
#     bot.register_next_step_handler(message, get_location)
# print(name)
# def get_location(message):
#     global location
#     location = message.text
#     bot.send_message(message.from_user.id, 'Какие зарплатные ожидания у кандидата?')
#     bot.register_next_step_handler(message, get_salary)
# print(location)
# def get_salary(message):
#     global salary
#     salary = message.text
#     bot.send_message(message.from_user.id, 'Какие форматы работы рассматривает кандидат')
#     bot.register_next_step_handler(message, get_work_mode)
# print(salary)
# def get_work_mode(message):
#     global work_mode
#     work_mode = message.text
#     bot.send_message(message.from_user.id, 'Укажи стэк кандидата')
#     bot.register_next_step_handler(message, get_stack)
# print(work_mode)
# def get_stack(message):
#     global stack
#     stack = message.text
#     bot.send_message(message.from_user.id, 'Укажи ссылку на резюме кандидата')
#     bot.register_next_step_handler(message, get_resume)
# print(stack)
# def get_resume(message):
#     global resume
#     resume = message.text
#     bot.send_message(message.from_user.id, 'комментарий')
#     bot.register_next_step_handler(message, get_coment)
# print(resume)
# def get_coment(message):
#     global coment
#     coment = message.text
#     bot.send_message(message.from_user.id, 'хэштег')
#     bot.register_next_step_handler(message, get_hashtag)
# print(coment)
# def get_hashtag(message):
#     global hashtag
#     hashtag = message.text
#     bot.send_message(message.from_user.id, 'Всё верно?')
#     bot.register_next_step_handler(message, check)
# print(hashtag)
def check (message, candidat=CANDIDAT):
    bot.send_message(message.chat.id, f'{candidat}')

@bot.message_handler(content_types=['text'])
def handle_text(message):
    bot.send_message(message.from_user.id, "Напиши /help")

bot.polling()