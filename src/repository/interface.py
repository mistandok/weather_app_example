from typing import Protocol

from psycopg2._psycopg import connection

from src.service.model.weather import Weather

type SupportedDBClient = connection


class RequestsHistoryRepoProtocol(Protocol):
    def save(self, conn: SupportedDBClient, weather: Weather):
        pass

    def get_history(self, conn: SupportedDBClient, last_n: int) -> list[Weather]:
        pass


class CityLogRepoProtocol(Protocol):
    def save(self, conn: SupportedDBClient, city: str):
        pass