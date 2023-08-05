import sys
import telebot
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup

from src.main import Diet
from src.telegram_bot.token import telegraf_token


sys.path.append('../')
bot = telebot.TeleBot(telegraf_token, parse_mode=None)
diet = Diet()


@bot.message_handler(commands=['start'])
def start_command(message):
    keyboard = [[InlineKeyboardButton("Get menu", callback_data='get_menu')]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    bot.send_message(message.chat.id, "Hi! Do you want to create a new menu?", reply_markup=reply_markup)


@bot.message_handler(commands=['help'])
def help_command(message):
    bot.send_message(message.chat.id, "Hi! This bot can create a diet from your favorite dishes. Please type /start to "
                                      "proceed...")


@bot.message_handler(commands=['get_menu'])
def menu_command(message):
    diet.set_menu()
    menu = diet.get_menu()
    bot.send_message(message.chat.id, menu)


@bot.message_handler(commands=['get_grocery_list'])
def grocery_list_command(message):
    diet.set_grocery_list()
    grocery_list = diet.get_grocery_list()
    bot.send_message(message.chat.id, grocery_list)

@bot.callback_query_handler(func=lambda call: True)
def button_callback(call):
    user_id = call.from_user.id
    if call.data == 'get_menu':
        diet.set_menu()
        menu_text = diet.get_menu()
        bot.send_message(chat_id=user_id, text=menu_text)
    elif call.data == 'get_grocery_list':
        diet.set_menu()
        grocery_list_text = diet.get_grocery_list()
        bot.send_message(chat_id=user_id, text=grocery_list_text)


bot.infinity_polling()
#
# sys.path.append('../')
#
# diet = Diet()
#
# # async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
# #     await context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")
#
#
# async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     user_id = update.effective_user.id
#     keyboard = [
#         [InlineKeyboardButton("Get menu", callback_data='get_menu')]
#         # [InlineKeyboardButton("Get grocery list",
#         #                       callback_data='get_grocery_list')]
#     ]
#     reply_markup = InlineKeyboardMarkup(keyboard)
#     await context.bot.send_message(
#         chat_id=user_id, text="Hi! Do you want to create a new menu?", reply_markup=reply_markup)
#
#
# if __name__ == '__main__':
#     bot = ApplicationBuilder().token(telegraf_token).build()
#
#     bot.add_handler(CommandHandler('start', start))
#
#
#     def get_menu(update):
#         diet.set_menu()
#         menu_text = diet.get_menu()
#         update.message.reply_text(menu_text)
#
#
#     def get_grocery_list(update):
#         diet.set_menu()
#         grocery_list_text = diet.get_grocery_list()
#         update.message.reply_text(grocery_list_text)
#
#
#     def button_callback(update, context):
#         query = update.callback_query
#         user_id = query.from_user.id
#         if query.data == 'get_menu':
#             diet.set_menu()
#             menu_text = diet.get_menu()
#             context.bot.send_message(chat_id=user_id, text=menu_text)
#         elif query.data == 'get_grocery_list':
#             diet.set_menu()
#             grocery_list_text = diet.get_grocery_list()
#             context.bot.send_message(chat_id=user_id, text=grocery_list_text)
#
#
#     bot.add_handler(CommandHandler('get_menu', get_menu))
#     bot.add_handler(CommandHandler('get_grocery_list', get_grocery_list))
#     bot.add_handler(CallbackQueryHandler(button_callback))
#
#     bot.run_polling()
