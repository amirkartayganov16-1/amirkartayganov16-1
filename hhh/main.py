from aiogram import Bot, executor, Dispatcher, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ParseMode
from decouple import config
import logging


TOKEN = config("TOKEN")
bot = Bot(TOKEN)
dp = Dispatcher(bot=bot)

@dp.message_handler(commands=['start'])
async def hello(message: types.Message):
    await bot.send_message(message.chat.id, f"Привет {message.from_user.full_name}")

@dp.message_handler(commands=['quiz'])
async def quiz_1(message: types.Message):
    question = "Какой стране принадлежит марка BMW?"
    answers = ['Японии', 'Казахстану', 'Америке', 'Германии']
    await bot.send_poll(message.chat.id,
                        question=question,
                        options=answers,
                        is_anonymous=False,
                        type='quiz',
                        correct_option_id=3
                        )
    question = "Какой области нет в Кыргызстане?"
    answers = ['Нарынской', 'Иссык-Кульской', 'Ташкентской', 'Ошской']
    await bot.send_poll(message.chat.id,
                        question=question,
                        options=answers,
                        is_anonymous=False,
                        type='quiz',
                        correct_option_id=2
                        )
@dp.message_handler(commands=['mem'])
async def mem_mem(message: types.Message):
    photo = open("media/cover_6.jpg, rb")
    await bot.send_photo(message.chat.id, photo=photo)

@dp.message_handler()
async def echo_message(message: types.Message):
    await message.answer(message.text)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=False)