import telebot
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup

from src.main import Diet
from src.telegram_bot.token import token


bot = telebot.TeleBot(token, parse_mode=None)


@bot.message_handler(commands=['start'])
def start_command(message):
    keyboard = [[InlineKeyboardButton("Get menu", callback_data='get_menu')]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    bot.send_message(message.chat.id, "Hi! Do you want to create a new menu?", reply_markup=reply_markup)


@bot.message_handler(commands=['help'])
def help_command(message):
    bot.send_message(message.chat.id, "Hi! This bot can create a diet from your favorite dishes. Please type /start to "
                                      "proceed...")


@bot.message_handler(commands=['menu'])
def menu_command(message):
    keyboard = [[InlineKeyboardButton("Get grocery list", callback_data='get_grocery_list')]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    diet = Diet()
    diet.set_menu()
    menu = diet.get_menu()
    bot.send_message(message.chat.id, menu, reply_markup=reply_markup)


@bot.message_handler(commands=['grocery_list'])
def grocery_list_command(message):
    diet = Diet()
    diet._set_ingredients_list()
    diet.set_grocery_list()
    grocery_list = diet.get_grocery_list()
    bot.send_message(message.chat.id, grocery_list)


@bot.message_handler(commands=['cheatmeal'])
def cheatmeal_command(message):
    diet = Diet()
    cheatmeal = diet.get_random_cheatmeal()
    bot.send_message(message.chat.id, cheatmeal)


@bot.message_handler(commands=['dishes'])
def dishes_command(message):
    diet = Diet()
    dishes = diet.get_dishes_list()
    bot.send_message(message.chat.id, dishes)

@bot.callback_query_handler(func=lambda call: True)
def button_callback(call):
    user_id = call.from_user.id
    if call.data == 'get_menu':
        keyboard = [[InlineKeyboardButton("Get grocery list", callback_data='get_grocery_list')]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        diet = Diet()
        diet.set_menu()
        menu_text = diet.get_menu()
        bot.send_message(chat_id=user_id, text=menu_text, reply_markup=reply_markup)
    elif call.data == 'get_grocery_list':
        diet = Diet()
        diet.set_grocery_list()
        grocery_list_text = diet.get_grocery_list()
        bot.send_message(chat_id=user_id, text=grocery_list_text)


bot.polling()
