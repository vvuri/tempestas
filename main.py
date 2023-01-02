import time

from app import app
from app.telegram import start_telegram_bot

if __name__ == '__main__':
    app.init()
    start_telegram_bot()
