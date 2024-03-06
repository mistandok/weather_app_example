from psycopg2._psycopg import connection

from src.repository.city_log.model.model import CITY_LOG_TABLE, CITY_NAME_COLUMN, COUNT_REQUESTS_COLUMN
from src.repository.interface import CityLogRepoProtocol


class CityLogRepo(CityLogRepoProtocol):
    def save(self, conn: connection, city: str):
        sql = f"""
            INSERT INTO {CITY_LOG_TABLE}
            ({CITY_NAME_COLUMN}, {COUNT_REQUESTS_COLUMN})
            VALUES (%s, %s)
            ON CONFLICT ({CITY_NAME_COLUMN}) DO UPDATE
            SET {COUNT_REQUESTS_COLUMN} = {CITY_LOG_TABLE}.{COUNT_REQUESTS_COLUMN} + 1
        """

        with conn.cursor() as cursor:
            cursor.execute(sql, (city, 1))
