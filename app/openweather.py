# https://openweathermap.org/
# http://api.openweathermap.org/data/2.5/find?q=Petersburg&type=like&APPID=*****
# Response:
# {'message': 'like', 'cod': '200', 'count': 2,
#   'list': [
#       {'id': 480562, 'name': 'Tula',
#       'coord': {'lat': 54.2044, 'lon': 37.6111},
#       'main': {'temp': 271.35, 'feels_like': 266.9, 'temp_min': 271.35, 'temp_max': 271.35, 'pressure': 1012, 'humidity': 97, 'sea_level': 1012, 'grnd_level': 992},
#       'dt': 1668553744,
#       'wind': {'speed': 3.68, 'deg': 125},
#       'sys': {'country': 'RU'},
#       'rain': None,
#       'snow': {'1h': 0.64},
#       'clouds': {'all': 100},
#       'weather': [{'id': 601, 'main': 'Snow', 'description': 'snow', 'icon': '13n'}]},
#       {'id': 480508, 'name': 'Tul’skaya Oblast’', 'coord': {'lat': 54, 'lon': 37.5}, 'main': {'temp': 270.77, 'feels_like': 266.1, 'temp_min': 270.77, 'temp_max': 270.77, 'pressure': 1012, 'humidity': 97, 'sea_level': 1012, 'grnd_level': 981}, 'dt': 1668553512, 'wind': {'speed': 3.8, 'deg': 119}, 'sys': {'country': 'RU'}, 'rain': None, 'snow': {'1h': 0.69}, 'clouds': {'all': 100}, 'weather': [{'id': 601, 'main': 'Snow', 'description': 'snow', 'icon': '13n'}]}]}

import json
import requests

from enum import Enum


class WindDirection(Enum):
    North = {
        'deg': 0,
        'ru': 'с'
    }
    Northeast = {
        'deg': 45,
        'ru': 'с-в'
    }
    East = {
        'deg': 90,
        'ru': 'в'
    }
    Southeast = {
        'deg': 135,
        'ru': 'ю-в'
    }
    South = {
        'deg': 180,
        'ru': 'ю'
    }
    Southwest = {
        'deg': 225,
        'ru': 'ю-з'
    }
    West = {
        'deg': 270,
        'ru': 'з'
    }
    Northwest = {
        'deg': 315,
        'ru': 'с-з'
    }

    def __init__(self, vals):
        self.deg = vals['deg']
        self.ru = vals['ru']


class OpenWeather:
    def __init__(self, config, logger):
        self.URL = "http://api.openweathermap.org/data/2.5/find"
        self.token = config['token']
        self.city = config['city']
        self.logger = logger

    def _parse_snow(self, d) -> str:
        # ToDo: {'1h': 0.64}
        res = "0"
        if d['1h']:
            res = str(d['1h'])
        return res

    def _parse_rain(self, d) -> str:
        # ToDo: None -> ?
        res = "0"
        return res

    def _parse_clouds(self, d) -> str:
        # ToDo: {'all': 100}
        res = "Ясно"
        if d['all'] > 80:
            res = "Облачно"
        elif d['all'] > 30:
            res = "Переменная облачность"
        return res

    def _parse_direction(self, degrees) -> str:
        degrees = round(degrees / 45) * 45
        if degrees == 360:
            degrees = 0
        for item in WindDirection:
                if item.deg == degrees:
                    return item.ru
        return ''

    def get_current_weather(self):
        current_temp = "null"

        payload = {
            'q': self.city,
            'type': 'like',
            'units': 'metric',
            'APPID': self.token
        }
        try:
            r = requests.get(self.URL, params=payload)

            try:
                response = json.loads(r.text)
                {'message': 'like', 'cod': '200', 'count': 2, 'list': [{'id': 480562, 'name': 'Tula', 'coord': {'lat': 54.2044, 'lon': 37.6111}, 'main': {'temp': 271.35, 'feels_like': 266.9, 'temp_min': 271.35, 'temp_max': 271.35, 'pressure': 1012, 'humidity': 97, 'sea_level': 1012, 'grnd_level': 992}, 'dt': 1668553744, 'wind': {'speed': 3.68, 'deg': 125}, 'sys': {'country': 'RU'}, 'rain': None, 'snow': {'1h': 0.64}, 'clouds': {'all': 100}, 'weather': [{'id': 601, 'main': 'Snow', 'description': 'snow', 'icon': '13n'}]}, {'id': 480508, 'name': 'Tul’skaya Oblast’', 'coord': {'lat': 54, 'lon': 37.5}, 'main': {'temp': 270.77, 'feels_like': 266.1, 'temp_min': 270.77, 'temp_max': 270.77, 'pressure': 1012, 'humidity': 97, 'sea_level': 1012, 'grnd_level': 981}, 'dt': 1668553512, 'wind': {'speed': 3.8, 'deg': 119}, 'sys': {'country': 'RU'}, 'rain': None, 'snow': {'1h': 0.69}, 'clouds': {'all': 100}, 'weather': [{'id': 601, 'main': 'Snow', 'description': 'snow', 'icon': '13n'}]}]}
                self.logger.debug(response)

                status_code = response['cod']
                if status_code == '200':
                    # find Tula
                    cities = ["{} ({})".format(d['name'], d['sys']['country']) for d in response['list']]
                    position = cities.count('Tula (RU)')

                    # temperatuer
                    t = response['list'][position]['main']
                    current_temp = str(round(float(t['temp'])))

                    # wind speed {'speed': 3.68, 'deg': 125}
                    wind = response['list'][position]['wind']['speed']
                    wind_direction = self._parse_direction(response['list'][position]['wind']['deg'])

                    # rain
                    rain = response['list'][position]['rain']

                    # snow
                    snow = self._parse_snow(response['list'][position]['snow'])

                    # clouds
                    clouds = self._parse_clouds(response['list'][position]['clouds'])
            except:
                self.logger.warn("No parse response from openweathermap.org")
                self.logger.warn("response: " + response)
        except:
            self.logger.warn("No response from openweathermap.org")
            self.logger.warn("response: " + r)
            self.logger.debug("request url: " + self.URL)

        return {'temp': current_temp, 'wind': wind, "wind_direction": wind_direction,
                "rain": rain, "snow": snow, "clouds": clouds}
