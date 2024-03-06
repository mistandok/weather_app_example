import dataclasses
import datetime
from enum import StrEnum


class WeatherConditions(StrEnum):
    THUNDERSTORM = "Гроза"
    DRIZZLE = "Изморось"
    RAIN = "Дождь"
    SNOW = "Снег"
    CLEAR = "Ясно"
    FOG = "Туман"
    CLOUDS = "Облачно"


@dataclasses.dataclass
class Weather:
    city_name: str
    weather_conditions: WeatherConditions
    temperature: float
    feels_like: float
    wind_speed: float
    timestamp: float
    timezone: int
    _time_with_tz: datetime.datetime = None

    def __post_init__(self):
        tz = datetime.timezone(datetime.timedelta(seconds=self.timezone))
        self._time_with_tz = datetime.datetime.fromtimestamp(self.timestamp, tz)

    @property
    def date(self):
        return datetime.datetime.fromtimestamp(self.timestamp)

    @property
    def datetime(self):
        return self._time_with_tz

    def __repr__(self):
        return f"""
            Город: {self.city_name},
            Погодные условия: {self.weather_conditions.value},
            Температура: {self.temperature} °C,
            Ощущается как: {self.feels_like} °C,
            Скорость ветра: {self.wind_speed} м/с,
            На время: {self.datetime}
        """
