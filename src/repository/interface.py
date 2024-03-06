from typing import Protocol

from psycopg2._psycopg import connection

from src.service.model.weather import Weather

# Обычно у всех баз есть какая-то сущность, через которую можно с базой общаться.
# Используем утиную типизацию питончка, чтобы не мучиться с созданием оберток над разными клиентами.
# Если надо поддерживать новый тип, то просто нужно добавить его сюда.
type SupportedDBClient = connection


# Соединение передаем в качестве аргумента методов, чтобы поддерживать транзакции,
# которые могут быть общими для нескольких репозиториев.
# для транзакций все операции должны выполнятся в одном соединении.
class RequestsHistoryRepoProtocol(Protocol):
    def save(self, conn: SupportedDBClient, weather: Weather):
        pass

    def get_history(self, conn: SupportedDBClient, last_n: int) -> list[Weather]:
        pass


class CityLogRepoProtocol(Protocol):
    def save(self, conn: SupportedDBClient, city: str):
        pass