from aiogram import Bot, Dispatcher, executor, types

from app.app import secret, logger, get_current_weather

token = secret['telegram']['token']

bot = Bot(token=token, parse_mode=types.ParseMode.HTML)
logger.debug("Init TelegramBot")

dp = Dispatcher(bot)


@dp.message_handler(commands="hi")
async def cmd_hi(message: types.Message):
    await message.answer("Прогноз подгоды в *Туле*", parse_mode="MarkdownV2")
    await message.answer("Для получения текущей погоды введите, */now*!", parse_mode="MarkdownV2")


@dp.message_handler(commands="now")
async def cmd_now(message: types.Message):
    t = get_current_weather()
    await message.answer("Погода в Туле:", parse_mode=types.ParseMode.HTML)
    await message.answer("Температура " + str(t['temp']), parse_mode=types.ParseMode.HTML)


def start_telegram_bot():
    logger.info("Run Telegram bot")
    # skip_updates - при перезапуске не обрабатывать старые сообщения
    executor.start_polling(dp, skip_updates=True)
