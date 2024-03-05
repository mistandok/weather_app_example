from typing import Protocol

from src.model.weather import Weather


class RequestHistoryRepository(Protocol):
    def save(self, weather: Weather):
        pass

    def get_history(self, last_n: int) -> list[Weather]:
        pass