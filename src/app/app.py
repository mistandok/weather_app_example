import os

from src.app.command import Command, GetWeatherForCityCommand, GetRequestsHistoryCommand, FinishCommand, PauseCommand
from src.app.initialiser import postgresql_connect
from src.client.openweather.openweather import OpenweatherClient
from src.config.config import PGSettings, OpenWeatherSettings
from src.error.error import WrongInputError, BaseAppError
from src.repository.city_log.repository import CityLogRepo
from src.repository.requests_history.repository import RequestsHistoryRepo
from src.service.weather.weather import WeatherService
from src.transaction.pg.transaction import PgTxAndConnManager


class App:
    def __init__(self, env_path: str):
        self._pg_settings = PGSettings(_env_file=env_path)
        self._openweather_settings = OpenWeatherSettings(_env_file=env_path)

        self._pause_command = PauseCommand()

        self._user_commands_map: dict[int, Command] = {}
        self._last_num = 1

    def start(self):
        weather_client = OpenweatherClient(self._openweather_settings.api_key)

        with postgresql_connect(self._pg_settings) as conn:
            conn_manager = PgTxAndConnManager(conn)
            request_history_repo = RequestsHistoryRepo()
            city_log_repo = CityLogRepo()
            service = WeatherService(conn_manager, weather_client, city_log_repo, request_history_repo)

            self._register_user_commands(
                GetWeatherForCityCommand(service, self._pause_command),
                GetRequestsHistoryCommand(service, self._pause_command),
                FinishCommand()
            )

            self._run_loop()

    def _register_user_commands(self, *commands: Command):
        for num, command in enumerate(commands, start=self._last_num):
            self._user_commands_map[num] = command

        self._last_num += len(commands)

    def _run_loop(self):
        while True:
            try:
                self._clear_terminal()
                self._print_menu()
                self._execute_command(self._get_command_num())
            except BaseAppError as e:
                print(f"\n{e}")
                self._pause_command.execute()
            except Exception as e:
                print(f"\nчто-то пошло не так :(: {e}")
                self._pause_command.execute()

    def _clear_terminal(self):
        os.system("clear")

    def _print_menu(self):
        for num, command in self._user_commands_map.items():
            print(f"{num}. {command}")
        print()

    def _execute_command(self, command_num: int):
        command = self._user_commands_map.get(command_num)
        command.execute()

    def _get_command_num(self):
        command_num = input("введите номер команды: ")
        return self._convert_command_num(command_num)

    def _convert_command_num(self, command_num: str) -> int:
        msg = "номер команды должен совпадать со списком команд."
        try:
            num = int(command_num)
        except ValueError:
            raise WrongInputError(msg)

        if num not in self._user_commands_map:
            raise WrongInputError(msg)

        return num
