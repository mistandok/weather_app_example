from src.client.interface import WeatherClientProtocol
from src.repository.interface import CityLogRepoProtocol, RequestsHistoryRepoProtocol
from src.service.model.weather import Weather
from src.service.interface import WeatherServiceProtocol
from src.transaction.interface import TxAndConnManagerProtocol


class WeatherService(WeatherServiceProtocol):
    def __init__(
            self,
            conn_manager: TxAndConnManagerProtocol,
            weather_client: WeatherClientProtocol,
            city_log_repo: CityLogRepoProtocol,
            requests_history_repo: RequestsHistoryRepoProtocol,
    ):
        self._conn_manager = conn_manager
        self._weather_client = weather_client
        self._city_log_repo = city_log_repo
        self._requests_history_repo = requests_history_repo

    def get_weather_for_city(self, city: str) -> Weather:
        weather = self._weather_client.get_weather_for_city(city)

        with self._conn_manager.transaction() as tx:
            self._requests_history_repo.save(tx, weather)
            self._city_log_repo.save(tx, weather.city_name)

        return weather

    def get_requests_history(self, last_n: int) -> list[Weather]:
        return self._requests_history_repo.get_history(self._conn_manager.connect(), last_n)
