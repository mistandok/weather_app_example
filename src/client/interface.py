from typing import Protocol

from src.service.model.weather import Weather


class WeatherClientProtocol(Protocol):
    def get_weather_for_city(self, city: str) -> Weather:
        pass
