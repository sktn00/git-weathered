import csv
import datetime as dt
import json

import requests

BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"
API_KEY = open("api_key.txt", "r").read()

city = input(str("Select the location desired: "))
unit = input("Select your desired unit (standard, metric or imperial): ").lower()
while unit not in ["standard", "metric", "imperial"]:
    unit = input(str("Error selecting unit, try again (standard, metric or imperial)"))

export_format = input("Select export format (csv, json or txt): ").lower()
while export_format not in ["csv", "json", "txt"]:
    export_format = input(
        "Invalid format. Select export format (csv, json or txt)"
    ).lower()

url = BASE_URL + "appid=" + API_KEY + "&q=" + city + "&units=" + unit
response = requests.get(url).json()

temp = response["main"]["temp"]
feels_like = response["main"]["feels_like"]
wind_speed = response["wind"]["speed"]
humidity = response["main"]["humidity"]
description = response["weather"][0]["description"]
sunrise_time = dt.datetime.fromtimestamp(response["sys"]["sunrise"], dt.UTC)
sunset_time = dt.datetime.fromtimestamp(response["sys"]["sunset"], dt.UTC)

weather_data = {
    "city": city,
    "temperature": f"{temp:.2f}",
    "feels_like": f"{feels_like:.2f}",
    "humidity": humidity,
    "wind_speed": wind_speed,
    "description": description,
    "sunrise": str(sunrise_time),
    "sunset": str(sunset_time),
}

if unit == "standard":
    weather_data["temp_unit"] = "K"
elif unit == "metric":
    weather_data["temp_unit"] = "C"
else:
    weather_data["temp_unit"] = "F"


def export_to_csv(data, filename):
    with open(filename, "w", newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=data.keys())
        writer.writeheader()
        writer.writerow(data)


def export_to_json(data, filename):
    with open(filename, "w", newline="") as jsonfile:
        json.dump(data, jsonfile, indent=4)


def export_to_txt(data, filename):
    with open(filename, "w", newline="") as txtfile:
        for key, value in data.items():
            txtfile.write(f"{key}: {value}\n")


filename = f"weather_data_{city}.{export_format}"

if export_format == "csv":
    export_to_csv(weather_data, filename)
elif export_format == "json":
    export_to_json(weather_data, filename)
else:
    export_to_txt(weather_data, filename)

print(f"Weather data has been exported to {filename}")

# Console output
print(f"Temperature in {city}: {temp:.2f}°{weather_data['temp_unit']}")
print(f"Temperature in {city} feels like: {feels_like:.2f}°{weather_data['temp_unit']}")
print(f"Humidity in {city}: {humidity}%")
print(f"Wind speed in {city}: {wind_speed}m/s")
print(f"General weather in {city}: {description}")
print(f"Sun rises in {city} at {sunrise_time} local time")
print(f"Sun sets in {city} at {sunset_time} local time")
