import argparse
import datetime

from src.client.openweather.openweather import OpenweatherClient
from src.config.config import PGSettings, OpenWeatherSettings
from src.app.initialisers import postgresql_connect
from src.model.weather import Weather, WeatherConditions
from src.repository.requests_history.repository import RequestsHistoryRepo


def get_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description='Script so useful.')
    parser.add_argument("--env", type=str, default="deploy/env/.env.local")

    return parser


if __name__ == "__main__":
    app_parser = get_parser()
    args = app_parser.parse_args()

    pg_settings = PGSettings(_env_file=args.env)
    openweather_settings = OpenWeatherSettings(_env_file=args.env)

    print(openweather_settings.api_key)

    client = OpenweatherClient(openweather_settings.api_key)

    cities = ["Москва", "Токио", "Владивосток", "Санкт-Петербург"]
    with postgresql_connect(pg_settings) as conn:
        request_history_repo = RequestsHistoryRepo(conn)
        # for city in cities:
        #     weather = client.get_weather_for_city(city)
        #     request_history_repo.save(weather)

        history = request_history_repo.get_history(4)
        for row in history:
            print(row)