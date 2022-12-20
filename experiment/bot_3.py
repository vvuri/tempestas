import yaml

from aiogram import Bot, Dispatcher, types

SECRET_FILE = '../secret.yaml'
token = None
with open(SECRET_FILE) as f:
    secret = yaml.full_load(f)
    token = secret['telegram']['token']

bot = Bot(token=token, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)
