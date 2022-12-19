# from telegram.ext.updater import Updater
# from telegram.update import Update
# from telegram.ext.callbackcontext import CallbackContext
# from telegram.ext.commandhandler import CommandHandler
import asyncio
import time
from typing import Any

import requests

from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardButton
import json

BTN_WEATHER = InlineKeyboardButton('Weather', callback_data='weather')


class TelegramBot():
    def __init__(self, config, logger):
        self.token = config['token']
        self.bot_name = config['name']
        self.bot_user = config['user']
        self.logger = logger
        self.URL = "https://api.telegram.org/bot" + self.token
        self.bot = Bot(token=self.token)
        self.loop = asyncio.get_event_loop()
        self.loop.run_until_complete(self.__async__init())

    async def __async__init(self):
        try:
            self.disp = Dispatcher(self.bot)
            self.disp.register_message_handler(self.start_handler, commands={"start", "restart"})
            await self.disp.start_polling()
        except:
            self.logger.warn("Telegram not init dispatcher")

    def __del__(self):
        self.bot.close()
        time.sleep(3)

    # def run(self):
    #     self.updater = Updater(self.token, use_context=True)
    #
    #     self.updater.dispatcher.add_handler(CommandHandler('start', self.start))
    #     self.updater.dispatcher.add_handler(CommandHandler('help', self.help))
    #
    #     self.updater.start_polling()
    #     self.logger.debug("run bot")
    #
    # def start(self, update: Update, context: CallbackContext):
    #     update.message.reply_text(
    #         "Enter the text you want to show to the user whenever they start the bot")
    #     self.logger.debug("start")
    #
    # def help(self, update: Update, context: CallbackContext):
    #     update.message.reply_text("Your Message")
    #     self.logger.debug("help")

    def _getRequest(self, path):
        r = requests.get(self.URL + path)
        self.logger.debug(r.status_code)
        try:
            response = json.loads(r.text)
            self.logger.debug(response)
        except:
            self.logger.warn("Telegram getMe response")
        return response

    def getMe(self) -> dict:
        return self._getRequest("/getMe")

    def getUpdates(self) -> dict:
        return self._getRequest("/getUpdates")

    async def say_hello(self):
        try:
            me = await self.bot.get_me()
            print(f"🤖 Hello, I'm {me.first_name}.\nHave a nice Day!")
        except:
            self.logger.warn("telegram bot say_hello error")

    async def start_handler(self, event: types.Message):
        await event.answer(
            f"Hello, {event.from_user.get_mention(as_html=True)} 👋!",
            parse_mode=types.ParseMode.HTML
        )

    async def handle(self) -> Any:
        await self.event.answer("Hello!")