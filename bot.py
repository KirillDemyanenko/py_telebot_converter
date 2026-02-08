from config import BOT_TOKEN
import telebot


def main():

    if not BOT_TOKEN:
        print('Bot token not set')
        return

    bot = telebot.TeleBot(BOT_TOKEN)

    @bot.message_handler(commands=['start'])
    def handle_start(message):
        bot.send_message(message.chat.id, "Привет! Я бот который умеет конвертировать все!")

    bot.infinity_polling()



if __name__ == '__main__':
    main()

