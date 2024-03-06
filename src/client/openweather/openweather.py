from datetime import timedelta
from http import HTTPStatus
from typing import Any

import requests

from src.client.interface import WeatherClientProtocol
from src.client.openweather.converter.converter import from_response_to_service_weather
from src.error.error import NotFoundError, RemoteServerTimeoutError, RemoteServerInternalError
from src.service.model.weather import Weather


REQUEST_URL = "https://api.openweathermap.org/data/2.5/weather"
Q_PARAM = "q"
APP_ID_PARAM = "APPID"
UNITS_PARAM = "units"
LANG_PARAM = "lang"


class OpenweatherClient(WeatherClientProtocol):
    def __init__(self, api_key: str):
        self._api_key = api_key

    def get_weather_for_city(self, city: str) -> Weather:
        try:
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
        except NotFoundError:
            raise NotFoundError(f"город '{city}' не найден")

        return from_response_to_service_weather(response)


def do_get_request(url: str, params: dict[str, Any], timeout: timedelta) -> dict[str, Any]:
    try:
        data = requests.get(url=url, params=params, timeout=timeout.seconds)
    except requests.Timeout:
        raise RemoteServerTimeoutError(f"{url} не отвечает")

    if data.status_code == HTTPStatus.NOT_FOUND:
        raise NotFoundError

    if data.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        raise RemoteServerInternalError(f"{url} не отвечает")

    response = data.json()
    return response
