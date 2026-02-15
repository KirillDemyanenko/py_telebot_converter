from config import BOT_TOKEN
import telebot
from handlers import *


def main():

    if not BOT_TOKEN:
        print('Bot token not set')
        return

    bot = telebot.TeleBot(BOT_TOKEN)

    register_handlers(bot)

    bot.infinity_polling()



if __name__ == '__main__':
    main()

