from config import BOT_TOKEN
import telebot

from utils import convert_miles_to_km


def main():

    if not BOT_TOKEN:
        print('Bot token not set')
        return

    bot = telebot.TeleBot(BOT_TOKEN)

    @bot.message_handler(commands=['start'])
    def handle_start(message):
        bot.send_message(message.chat.id, "Привет! Я бот который умеет конвертировать все!")

    @bot.message_handler(commands=['help'])
    def handle_help(message):
        bot.send_message(message.chat.id, "Вот список команд, которые я знаю:\n/start\n/help\n/miles_to_km")

    @bot.message_handler(commands=['miles_to_km'])
    def handle_miles_to_km(message: telebot.types.Message):
        _, miles = message.text.split()
        try:
            miles = float(miles)
            bot.send_message(message.chat.id, f"{miles} миль = {convert_miles_to_km(miles)} километров")
        except ValueError:
            bot.send_message(message.chat.id, "Неверно введены данные.")

    bot.infinity_polling()



if __name__ == '__main__':
    main()

