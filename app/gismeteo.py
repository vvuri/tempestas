# work with https://www.gismeteo.ru/api/
import requests


class Gismeteo:
    def __init__(self):
        self.URL = "https://api.gismeteo.net/v2/weather/current"
        self.LANGUAGE = "ru"
        self.latitude = "54.21"
        self.longitude = "37.59"
        self.TOKEN = "56b30cb255.3443075"

    def get_current_weather(self):
        payload = {'latitude': self.latitude, 'longitude': self.latitude, 'lang': self.LANGUAGE}
        headers = {'X-Gismeteo-Token': self.TOKEN}
        r = requests.get(self.URL, params=payload, headers=headers)
        print(r.url)
        print(r.text)
        # {"meta":{"message":"Недействительный токен. Проверьте заголовок 'X-Gismeteo-Token'","code":401},"response":{}}
