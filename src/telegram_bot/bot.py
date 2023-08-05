from token import telegraf_token
from bin.index import Diet
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler

import sys
sys.path.append('../')


bot = Updater(token=telegraf_token, use_context=True)
diet = Diet()


def start(update, context):
    user_id = update.effective_user.id
    print(f'started: {user_id}')
    keyboard = [
        [InlineKeyboardButton("Get menu", callback_data='get_menu')],
        [InlineKeyboardButton("Get grocery list",
                              callback_data='get_grocery_list')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    context.bot.send_message(
        chat_id=user_id, text="Hi! Do you want to create a new menu?", reply_markup=reply_markup)


def get_menu(update):
    diet.set_menu()
    menu_text = diet.get_menu()
    update.message.reply_text(menu_text)


def get_grocery_list(update):
    diet.set_menu()
    grocery_list_text = diet.get_grocery_list()
    update.message.reply_text(grocery_list_text)


def button_callback(update, context):
    query = update.callback_query
    user_id = query.from_user.id
    if query.data == 'get_menu':
        diet.set_menu()
        menu_text = diet.get_menu()
        context.bot.send_message(chat_id=user_id, text=menu_text)
    elif query.data == 'get_grocery_list':
        diet.set_menu()
        grocery_list_text = diet.get_grocery_list()
        context.bot.send_message(chat_id=user_id, text=grocery_list_text)


bot.dispatcher.add_handler(CommandHandler('start', start))
bot.dispatcher.add_handler(CommandHandler('get_menu', get_menu))
bot.dispatcher.add_handler(CommandHandler('get_grocery_list', get_grocery_list))
bot.dispatcher.add_handler(CallbackQueryHandler(button_callback))

bot.start_polling()
bot.idle()
