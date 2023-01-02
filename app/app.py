import logging
import os.path

from .config import LOG_DIR
# from .gismeteo import Gismeteo
from .openweather import OpenWeather
from .helper import load_secrets

logger = logging.getLogger("app")
logger.setLevel(logging.DEBUG)

if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

handler = logging.StreamHandler()
handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.debug('init logger')

secret = load_secrets()
openweather = None


def init():
    logger.debug("run: start")

    # gismeteo = Gismeteo()
    # gismeteo.get_current_weather()

    openweather = OpenWeather(secret['openweather'], logger)

    # logger.info(cur_temp)

    logger.info("Telegram bot started")


def get_current_weather():
    # ToDo: work with memory catch
    cur_temp = openweather.get_current_weather()
    logger.debug(cur_temp)
    return cur_temp
