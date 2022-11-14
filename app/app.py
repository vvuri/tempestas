import logging
import os.path
import yaml

from .config import LOG_DIR, SECRET_FILE
from .gismeteo import Gismeteo
from .openweather import OpenWeather

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


def load_secrets():
    with open(SECRET_FILE) as f:
        return yaml.full_load(f)


def run():
    logger.debug("run: start")

    secret = load_secrets()

    # gismeteo = Gismeteo()
    # gismeteo.get_current_weather()

    openweather = OpenWeather(secret['openweather'], logger)
    cur_temp = openweather.get_current_weather()

    logger.info(cur_temp)
