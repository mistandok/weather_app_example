from datetime import timedelta
from typing import Any

import requests
from requests import Session, Request

from src.client.interfaces import WeatherSearcher
from src.client.openweather.converter.converter import from_response_to_service_weather
from src.model.weather import Weather


REQUEST_URL = "https://api.openweathermap.org/data/2.5/weather"
Q_PARAM = "q"
APP_ID_PARAM = "APPID"
UNITS_PARAM = "units"
LANG_PARAM = "lang"


class OpenweatherClient(WeatherSearcher):
    def __init__(self, api_key: str):
        self._api_key = api_key

    def get_weather_for_city(self, city: str) -> Weather:
        response = do_get_request(
            REQUEST_URL,
            params={
                Q_PARAM: city,
                APP_ID_PARAM: self._api_key,
                UNITS_PARAM: "metric",
                LANG_PARAM: "ru",
            },
            timeout=timedelta(seconds=2)
        )

        return from_response_to_service_weather(response)


def do_get_request(url: str, params: dict[str, Any], timeout: timedelta) -> dict[str, Any]:
    data = requests.get(url=url, params=params, timeout=timeout.seconds)
    response = data.json()
    return response
