import datetime as dt

import requests

BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"
API_KEY = open("api_key.txt", "r").read()

city = input(str("Select the location desired: "))

unit = input("Select your desired unit (standard, metric or imperial): ")
while unit != "standard" and unit != "metric" and unit != "imperial":
    unit = input(str("Error selecting unit, try again (standard, metric or imperial)"))

url = BASE_URL + "appid=" + API_KEY + "&q=" + city + "&units=" + unit
response = requests.get(url).json()

temp = response["main"]["temp"]
feels_like = response["main"]["feels_like"]
wind_speed = response["wind"]["speed"]
humidity = response["main"]["humidity"]
description = response["weather"][0]["description"]
sunrise_time = dt.datetime.fromtimestamp(response["sys"]["sunrise"], dt.UTC)
sunset_time = dt.datetime.fromtimestamp(response["sys"]["sunset"], dt.UTC)

if unit == "standard":
    print(f"Temperature in {city}: {temp:.2f}°K")
    print(f"Temperature in {city} feels like: {feels_like:.2f}°K")
elif unit == "metric":
    print(f"Temperature in {city}: {temp:.2f}°C")
    print(f"Temperature in {city} feels like: {feels_like:.2f}°C")
else:
    print(f"Temperature in {city}: {temp:.2f}°F")
    print(f"Temperature in {city} feels like: {feels_like:.2f}°F")

print(f"Humidity in {city}: {humidity}%")
print(f"Wind speed in {city}: {wind_speed}m/s")
print(f"General weather in {city}: {description}")
print(f"Sun rises in {city} at {sunrise_time} local time")
print(f"Sun sets in {city} at {sunset_time} local time")
