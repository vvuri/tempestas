import yaml

from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from aiogram.types import Message
from aiogram.dispatcher.middlewares import BaseMiddleware


async def cmd_hi(message: types.Message):
    await message.reply("Отличный выбор!")
    # await message.answer("Hello, world!")

SECRET_FILE = '../secret.yaml'
token = None
with open(SECRET_FILE) as f:
    secret = yaml.full_load(f)
    token = secret['telegram']['token']


# async def handler(message: Message, text: str):
#     await message.answer(text)

def generate_text():
    return "generated text"


async def handler(message: Message):
    text = generate_text()
    await message.answer(text)


class YourMiddleware(BaseMiddleware):
    async def on_pre_process_message(self, message: Message, data: dict):
        # `text` is a name of var passed to handler
        data["text"] = generate_text()


bot = Bot(token=token, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)
dp.middleware.setup(YourMiddleware())

executor.start_polling(dp, skip_updates=True)
