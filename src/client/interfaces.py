from typing import Protocol

from src.model.weather import Weather


class WeatherSearcher(Protocol):
    def get_weather_for_city(self, city: str) -> Weather:
        pass
