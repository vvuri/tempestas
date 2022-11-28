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
    await message.answer("Принято", reply_markup=types.ReplyKeyboardRemove())

@dp.message_handler(lambda message: message.text == "Cancel")
async def without_puree(message: types.Message):
    await message.reply("Так...")
    await message.reply("Отмена", reply_markup=types.ReplyKeyboardRemove())

@dp.message_handler(commands="special")
async def cmd_special_buttons(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(types.KeyboardButton(text="Запросить геолокацию", request_location=True))
    keyboard.add(types.KeyboardButton(text="Запросить контакт", request_contact=True))
    keyboard.add(types.KeyboardButton(text="Создать викторину",
                                      request_poll=types.KeyboardButtonPollType(type=types.PollType.QUIZ)))
    await message.answer("Выберите действие:", reply_markup=keyboard)

# inline button with message
@dp.message_handler(commands="inline")
async def cmd_inline_url(message: types.Message):
    buttons = [
        types.InlineKeyboardButton(text="GitHub", url="https://github.com"),
        types.InlineKeyboardButton(text="Оф. канал Telegram", url="tg://resolve?domain=telegram")
    ]
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(*buttons)
    await message.answer("Кнопки-ссылки", reply_markup=keyboard)

executor.start_polling(dp, skip_updates=True)
