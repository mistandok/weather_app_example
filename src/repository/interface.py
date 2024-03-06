from typing import Protocol

from psycopg2._psycopg import connection

from src.service.model.weather import Weather


class RequestsHistoryRepoProtocol(Protocol):
    def save(self, conn: connection, weather: Weather):
        pass

    def get_history(self, conn: connection, last_n: int) -> list[Weather]:
        pass


class CityLogRepoProtocol(Protocol):
    def save(self, conn: connection, city: str):
        pass