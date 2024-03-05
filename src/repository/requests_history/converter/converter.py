import datetime

from psycopg2.extras import DictRow

from src.model.weather import Weather, WeatherConditions
from src.repository.requests_history.model.model import CITY_NAME_COLUMN, WEATHER_CONDITIONS_COLUMN, TEMPERATURE_COLUMN, \
    FEELS_LIKE_COLUMN, WIND_SPEED_COLUMN, TIME_COLUMN, TIMEZONE_COLUMN


def _from_repo_weather_to_service_weather(repo_weather: DictRow) -> Weather:
    return Weather(
        city_name=repo_weather.get(CITY_NAME_COLUMN),
        weather_conditions=WeatherConditions(repo_weather.get(WEATHER_CONDITIONS_COLUMN)),
        temperature=repo_weather.get(TEMPERATURE_COLUMN),
        feels_like=repo_weather.get(FEELS_LIKE_COLUMN),
        wind_speed=repo_weather.get(WIND_SPEED_COLUMN),
        timestamp=datetime.datetime.timestamp(repo_weather.get(TIME_COLUMN)),
        timezone=int(repo_weather.get(TIMEZONE_COLUMN)),
    )
