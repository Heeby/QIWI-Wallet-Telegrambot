import logging
from aiogram import Bot, Dispatcher, executor, types

logging.basicConfig(level=logging.INFO)

from os import getenv
import DataBaseAPI.Telegram_DB
import Core

API_TOKEN = getenv("telegram_token")
phone = getenv("phone")  # TODO Less dependences .Use the same phone as in QIWI_API

# bot = telebot.TeleBot(API_TOKEN)
# @bot.message_handler(commands=['help', 'start'])
# def send_welcome(message):
#     bot.reply_to(message, """Привет. Я бот - кошелёк.
#     Вы можете хранить ваши деньги, используя меня. Напиши /deposit (/d) что бы внести средства. """)
#
# @bot.message_handler(commands=["deposit", "d"])
# def send_welcome(message):
#     bot.reply_to(message, f"""Что бы пополнить счёт отправтье необходимую сумму на счёт киви {phone}.
#                     В коментариях укажите {Core.generate_code(message.from.id)}""")

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


# Хэндлер на команду /start
@dp.message_handler(commands=["start", "help"])
async def cmd_start(message: types.Message):
    poll_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    poll_keyboard.add(types.KeyboardButton(text="/deposit",
                                           request_poll=types.KeyboardButtonPollType(type=types.PollType.QUIZ)))
    poll_keyboard.add(types.KeyboardButton(text="/balance"))
    await message.answer("""Привет. Я бот - кошелёк. 
    Вы можете хранить ваши деньги, используя меня. Напиши /deposit (/d) что бы внести средства.""", reply_markup=poll_keyboard)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
