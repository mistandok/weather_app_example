from src.service.model.weather import Weather, WeatherConditions


def from_response_to_service_weather(response: dict[str, any]) -> Weather:
    return Weather(
        city_name=response.get("name"),
        weather_conditions=from_response_weather_id_to_weather_condition(_get_weather_id(response)),
        temperature=response.get("main").get("temp"),
        feels_like=response.get("main").get("feels_like"),
        wind_speed=response.get("wind").get("speed"),
        timestamp=response.get("dt"),
        timezone=response.get("timezone"),
    )


def from_response_weather_id_to_weather_condition(weather_id: int) -> WeatherConditions:
    weather_types = {
        "1": WeatherConditions.THUNDERSTORM,
        "3": WeatherConditions.DRIZZLE,
        "5": WeatherConditions.RAIN,
        "6": WeatherConditions.SNOW,
        "7": WeatherConditions.FOG,
        "800": WeatherConditions.CLEAR,
        "80": WeatherConditions.CLOUDS
    }
    for code, weather_condition in weather_types.items():
        if str(weather_id).startswith(code):
            return weather_condition


def _get_weather_id(response: dict[str, any]) -> int:
    return response.get("weather")[0].get("id")
