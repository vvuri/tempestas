# work with https://www.gismeteo.ru/api/

class Gismeteo:
    def __init__(self):
        self.URL = "https://api.gismeteo.net/v2/weather/current/4368/?lang=ru"
        self.LANGUAGE = "ru"
        self.latitude = "54.21"
        self.longitude = "37.59"
        # https: // api.gismeteo.net / v2 / search / cities /?latitude = 54.35 & longitude = 52.52 & limit = 10
        self.TOKEN = "56b30cb255.3443075"
        pass

    def _url(self) -> str:
        full_url = ""

    def get_current_(self):
        pass

    # curl -H 'X-Gismeteo-Token: 56b30cb255.3443075' 'https://api.gismeteo.net/v2/search/cities/?latitude=54.35&longitude=52.52&limit=10'
    # curl -H 'X-Gismeteo-Token: 56b30cb255.3443075' 'https://api.gismeteo.net/v2/search/cities/?latitude=54.21&longitude=37.59&limit=10'