from aiogram.dispatcher.filters import Text

import yaml

from aiogram import types, Bot, Dispatcher, executor, types
import aiogram.utils.markdown as fmt

SECRET_FILE = '../secret.yaml'
token = None
with open(SECRET_FILE) as f:
     secret = yaml.full_load(f)
     token = secret['telegram']['token']

bot = Bot(token=token, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)

@dp.message_handler(commands="hi")
async def cmd_hi(message: types.Message):
     await message.answer("Hello, <b>world</b>!", parse_mode=types.ParseMode.HTML)
     # или
     await message.answer("Hello, *world*\!", parse_mode="MarkdownV2")

@dp.message_handler(commands="apple")
async def cmd_hi(message: types.Message):
     await message.answer(
        fmt.text(
            fmt.text(fmt.hunderline("Яблоки"), ", вес 1 кг."),
            fmt.text("Старая цена:", fmt.hstrikethrough(50), "рублей"),
            fmt.text("Новая цена:", fmt.hbold(25), "рублей"),
            sep="\n"
        ), parse_mode="HTML"
     )

# ============== buttons ================

@dp.message_handler(commands="start")
async def cmd_start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["Ok", "Cancel"]
    keyboard.add(*buttons)
    await message.answer("Return: ", reply_markup=keyboard)

@dp.message_handler(Text(equals="Ok"))
async def with_puree(message: types.Message):
    await message.reply("Отличный выбор!")

@dp.message_handler(lambda message: message.text == "Cancel")
async def without_puree(message: types.Message):
    await message.reply("Так...")

# @dp.message_handler(commands=['start', 'weather', 'now'])
# async def show_weather(message: types.Message):
#     await message.answer(text="start-weather", reply_markup=inline_keyboard.)

executor.start_polling(dp, skip_updates=True)
