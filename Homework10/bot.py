import telebot

API_TOKEN = ''
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def handle_text(message): 
    msg_num_1 = bot.send_message(message.chat.id, 'Введите 1 число') 
    bot.register_next_step_handler(msg_num_1, step_1)

def step_1(message):
   global num_1;
   num_1 = message.text
   msg_operation = bot.send_message(message.chat.id, 'Введите  действие: + - * /')
   bot.register_next_step_handler(msg_operation, step_2)
   
def step_2(message):
    global operation;
    operation = message.text      
    msg_num_2 = bot.send_message(message.chat.id, 'Введите 2 число')
    bot.register_next_step_handler(msg_num_2, step_3)
    
def step_3(message):
    global num_2;
    num_2 = message.text
    if operation == "+":
        result = int(num_1) + int(num_2)
        bot.send_message(message.chat.id, result)
    elif operation == "-":
        result = int(num_1) - int(num_2)
        bot.send_message(message.chat.id, result)
    elif operation == "*":
        result = int(num_1) * int(num_2)
        bot.send_message(message.chat.id, result)
    elif operation == "/": 
        result = int(num_1) / int(num_2)
        bot.send_message(message.chat.id, result)
    else:
        bot.send_message(message.chat.id, "ошибка введите /start")
    
bot.polling(none_stop = True) 