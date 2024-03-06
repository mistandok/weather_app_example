from typing import Protocol

from src.service.model.weather import Weather


class WeatherServiceProtocol(Protocol):
    def get_weather_for_city(self, city: str) -> Weather:
        pass

    def get_requests_history(self, last_n: int) -> list[Weather]:
        pass
