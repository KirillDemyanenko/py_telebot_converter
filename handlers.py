import math

import telebot

from utils import convert_miles_to_km, calculator, is_save_question

calculator_actions = ('Математический пример', 'Квадратный корень из числа')


def register_handlers(bot: telebot.TeleBot):
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

    def enter_question_step(message: telebot.types.Message):
        question = message.text

        if is_save_question(question):
            result = calculator(question)
            bot.send_message(message.chat.id, f"{question} = {result}")
        else:
            bot.send_message(message.chat.id, "Пример может содержать только математические операции и цифры")

    def enter_sqrt_step(message: telebot.types.Message):
        question = message.text.strip()

        if question.isdigit():
            result = math.sqrt(int(question))
            bot.send_message(message.chat.id, f"Квадратный корень из {question} равен {result}")
        else:
            bot.send_message(message.chat.id, "Пример может содержать только цифры")

    @bot.message_handler(commands=['calculator'])
    def handle_calculator(message: telebot.types.Message):
        kb = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        for text in calculator_actions:
            kb.add(telebot.types.KeyboardButton(text))
        bot.send_message(message.chat.id,
                         "Калькулятор\nСписок операций:\n+ : сложение\n/ : деление\n- : вычитание\n* : умножение\n",
                         reply_markup=kb)

    @bot.message_handler(func=lambda message: True)
    def handle_all(message: telebot.types.Message):
        if message.text == calculator_actions[0]:
            bot.send_message(message.chat.id, "Введите пример")
            bot.register_next_step_handler(message, enter_question_step)
        elif message.text == calculator_actions[1]:
            bot.send_message(message.chat.id, "Введите число")
            bot.register_next_step_handler(message, enter_sqrt_step)