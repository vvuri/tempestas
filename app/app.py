import logging
import os.path
import yaml

from .config import LOG_DIR
from .gismeteo import Gismeteo

logger = logging.getLogger("app")
logger.setLevel(logging.DEBUG)

if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

handler = logging.StreamHandler()
handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

logger.info('message from main module')

gismeteo = Gismeteo()

def load_secrets():
    pass

def run():
    print("Run server")
    gismeteo.get_current_weather()
