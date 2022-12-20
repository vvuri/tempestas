import yaml
from aiogram import Bot, Dispatcher, executor, types

SECRET_FILE = '../secret.yaml'


def run_telegram_bot():
    # token = None
    with open(SECRET_FILE) as f:
        secret = yaml.full_load(f)
        token = secret['telegram']['token']

    bot = Bot(token=token, parse_mode=types.ParseMode.HTML)
    dp = Dispatcher(bot)

    @dp.message_handler(commands="hi")
    async def cmd_hi(message: types.Message):
        await message.answer("Hello, <b>world</b>!", parse_mode=types.ParseMode.HTML)
        await message.answer("Hello, *world*!", parse_mode="MarkdownV2")

    @dp.message_handler(commands="start")
    async def cmd_start(message: types.Message):
        await message.answer("Weather Bot started")

    executor.start_polling(dp, skip_updates=True)


run_telegram_bot()
