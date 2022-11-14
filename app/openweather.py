# https://openweathermap.org/
# http://api.openweathermap.org/data/2.5/find?q=Petersburg&type=like&APPID=*****

import json
import requests


class OpenWeather:
    def __init__(self, config, logger):
        self.URL = "http://api.openweathermap.org/data/2.5/find"
        self.token = config['token']
        self.city = config['city']
        self.logger = logger

    def get_current_weather(self):
        current_temp = "null"

        payload = {
            'q': self.city,
            'type': 'like',
            'APPID': self.token
        }
        try:
            r = requests.get(self.URL, params=payload)

            try:
                response = json.loads(r.text)
                self.logger.debug(response)

                status_code = response['cod']

                if status_code == '200':
                    # ToDo: 0 -> 'name': 'Tula'
                    t = response['list'][0]['main']
                    current_temp = str(round(float(t['temp']) - 273))
                    wind = response['list'][0]['wind']['speed']
                    # ToDo: rain
                    # ToDo: snow
            except:
                self.logger.warn("No parse response from openweathermap.org")
                self.logger.warn("response: " + response)
        except:
            self.logger.warn("No response from openweathermap.org")
            self.logger.warn("response: " + r)
            self.logger.debug("request url: " + self.URL)

        return {'temp': current_temp, 'wind': wind}
