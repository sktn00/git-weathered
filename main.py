import datetime as dt

import requests

BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"
API_KEY = open("api_key.txt", "r").read()

city = input(str("Select the location desired: "))


def kelvin_to_celsius_fahrenheit(kelvin):
    celsius = kelvin - 273.15
    fahrenheit = celsius * (9 / 5) + 32
    return celsius, fahrenheit


url = BASE_URL + "appid=" + API_KEY + "&q=" + city
response = requests.get(url).json()

temp_kelvin = response["main"]["temp"]
temp_celsius, temp_fahrenheit = kelvin_to_celsius_fahrenheit(temp_kelvin)
fls_lk_kelvin = response["main"]["feels_like"]
feels_like_celsius, feels_like_fahrenheit = kelvin_to_celsius_fahrenheit(fls_lk_kelvin)
wind_speed = response["wind"]["speed"]
humidity = response["main"]["humidity"]
description = response["weather"][0]["description"]
sunrise_time = dt.datetime.fromtimestamp(response["sys"]["sunrise"], dt.UTC)
sunset_time = dt.datetime.fromtimestamp(response["sys"]["sunset"], dt.UTC)

print(f"Temperature in {city}: {temp_celsius:.2f}ºC or {temp_fahrenheit:.2f}ºF")
print(
    f"Temperature in {city} feels like: "
    f"{feels_like_celsius:.2f}ºC or "
    f"{feels_like_fahrenheit:.2f}ºF"
)
print(f"Humidity in {city}: {humidity}%")
print(f"Wind speed in {city}: {wind_speed}m/s")
print(f"General weather in {city}: {description}")
print(f"Sun rises in {city} at {sunrise_time} local time")
print(f"Sun sets in {city} at {sunset_time} local time")
