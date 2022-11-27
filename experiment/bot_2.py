import yaml

from aiogram import types, Bot, Dispatcher, executor, types

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

executor.start_polling(dp, skip_updates=True)
