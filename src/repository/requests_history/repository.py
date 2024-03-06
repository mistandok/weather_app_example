from psycopg2._psycopg import connection
from psycopg2.extras import DictCursor

from src.service.model.weather import Weather
from src.repository.interface import RequestsHistoryRepoProtocol
from src.repository.requests_history.converter.converter import from_repo_weather_to_service_weather
from src.repository.requests_history.model.model import REQUEST_HISTORY_TABLE, CITY_NAME_COLUMN, \
    WEATHER_CONDITIONS_COLUMN, TEMPERATURE_COLUMN, TIME_COLUMN, TIMEZONE_COLUMN, WIND_SPEED_COLUMN, FEELS_LIKE_COLUMN, \
    ID_COLUMN


class RequestsHistoryRepo(RequestsHistoryRepoProtocol):
    def save(self, conn: connection, weather: Weather):
        sql = f"""
            INSERT INTO {REQUEST_HISTORY_TABLE}
            ({CITY_NAME_COLUMN}, {WEATHER_CONDITIONS_COLUMN}, {TEMPERATURE_COLUMN},
            {FEELS_LIKE_COLUMN}, {WIND_SPEED_COLUMN}, {TIME_COLUMN}, {TIMEZONE_COLUMN})
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """

        with conn.cursor() as cursor:
            cursor.execute(
                sql,
                (
                    weather.city_name, weather.weather_conditions.value, weather.temperature,
                    weather.feels_like, weather.wind_speed, weather.date, weather.timezone,
                )
            )

    def get_history(self, conn: connection, last_n: int) -> list[Weather]:
        sql = f"""
            SELECT 
                {CITY_NAME_COLUMN},
                {WEATHER_CONDITIONS_COLUMN},
                {TEMPERATURE_COLUMN},
                {FEELS_LIKE_COLUMN},
                {WIND_SPEED_COLUMN},
                {TIME_COLUMN},
                {TIMEZONE_COLUMN}
            FROM
                {REQUEST_HISTORY_TABLE}
            ORDER BY {ID_COLUMN} DESC
            LIMIT %s
        """

        requests_history: list[Weather] = []

        with conn.cursor(cursor_factory=DictCursor) as cursor:
            cursor.execute(sql, (last_n,))
            result = cursor.fetchall()
            for row in result:
                requests_history.append(from_repo_weather_to_service_weather(row))

        return requests_history
