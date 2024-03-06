from abc import ABC
from typing import Protocol

from src.service.interface import WeatherServiceProtocol


class Command(Protocol):
    def execute(self):
        raise NotImplementedError()

    def __str__(self) -> str:
        raise NotImplementedError("необходимо ввести описание команды")


class GetWeatherForCityCommand(Command):
    def __init__(self, service: WeatherServiceProtocol, next_command: None | Command = None):
        self._service = service
        self._next_command = next_command

    def execute(self):
        city = input("введите город: ")
        weather = self._service.get_weather_for_city(city)
        print()
        print(weather)
        print()

        if self._next_command:
            self._next_command.execute()

    def __str__(self):
        return "получить погоду по названию города."


class GetRequestsHistoryCommand(Command):
    def __init__(self, service: WeatherServiceProtocol, next_command: None | Command = None):
        self._service = service
        self._next_command = next_command

    def execute(self):
        last_n = int(input("введите количество запросов: "))
        weather_history = self._service.get_requests_history(last_n)

        for weather in weather_history:
            print(weather)
            print()

        if self._next_command:
            self._next_command.execute()

    def __str__(self):
        return "получить историю последних n запросов."


class FinishCommand(Command):
    def execute(self):
        exit(0)

    def __str__(self):
        return "завершить работу программы"


class PauseCommand(Command):
    def execute(self):
        input("\nвведите enter, чтобы продолжить")
