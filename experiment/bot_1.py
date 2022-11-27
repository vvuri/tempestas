import asyncio
import logging

import yaml
from aiogram import Bot, Dispatcher, executor, types

SECRET_FILE = '../secret.yaml'
token = None
with open(SECRET_FILE) as f:
     secret = yaml.full_load(f)
     token = secret['telegram']['token']

# Объект бота
bot = Bot(token=token)

# Диспетчер для бота
dp = Dispatcher(bot)

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)


# Хэндлер на команду /test1
@dp.message_handler(commands="test1")
async def cmd_test1(message: types.Message):
    await message.reply("Test 1")

# или можно делать без декоратора
# # Хэндлер на команду /test2
# async def cmd_test2(message: types.Message):
#     await message.reply("Test 2")
#
# # Где-то в другом месте...
# dp.register_message_handler(cmd_test2, commands="test2")

@dp.message_handler(commands="test2")
async def cmd_test2(message: types.Message):
    await message.answer("Test 2")

@dp.message_handler(commands="dice")
async def cmd_dice(message: types.Message):
    await message.answer_dice(emoji="🎲")

# обработка исключений - вместо try
@dp.message_handler(commands="block")
async def cmd_block(message: types.Message):
    await asyncio.sleep(10.0)  # Здоровый сон на 10 секунд
    await message.reply("Вы заблокированы")

# if __name__ == "__main__":
    # Запуск бота
executor.start_polling(dp, skip_updates=True)
