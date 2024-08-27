import csv
import datetime as dt
import json

import requests

BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"
API_KEY = open("api_key.txt", "r").read()


def show_help():
    help_message = """
    Weather Fetching Program:
    -----------------------------------
    This program retrieves weather data from the OpenWeatherMap API for a specified city.

    Arguments:
    - City: Name of the city for which you want to retrieve weather data.
    - Unit: Desired unit of temperature. Options: 'standard' (Kelvin), 'metric' (Celsius), 'imperial' (Fahrenheit).
    - Export format: Format to export the weather data. Options: 'csv', 'json', 'txt'.
    
    Example usage:
    > python weather_program.py
    
    Follow the prompts to input city, unit, and export format.
    -----------------------------------
    """  # noqa: E501
    print(help_message)


def handle_api_error(response):
    if response.status_code != 200:
        error_data = response.json()
        error_code = error_data.get("cod", "Unknown")
        error_message = error_data.get("message", "No error message provided")

        # Handling specific error codes
        if error_code == 400:
            print(f"Error {error_code}: Bad Request - {error_message}")
        elif error_code == 401:
            print(f"Error {error_code}: Unauthorized - Check your API key.")
        elif error_code == 429:
            print(f"Error {error_code}: Too Many Requests - Please try again later.")
        else:
            print(f"Error {error_code}: {error_message}")

        return False
    return True


def fetch_weather_data(city, unit):
    url = BASE_URL + "appid=" + API_KEY + "&q=" + city + "&units=" + unit
    try:
        response = requests.get(url)
        if not handle_api_error(response):
            return None
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Failed to connect to the weather service: {e}")
        return None


def export_to_csv(data, filename):
    with open(filename, "w", newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=data.keys())
        writer.writeheader()
        writer.writerow(data)


def export_to_json(data, filename):
    with open(filename, "w", newline="") as jsonfile:
        json.dump(data, jsonfile, indent=4)


def export_to_txt(data, filename):
    with open(filename, "w") as txtfile:
        for key, value in data.items():
            txtfile.write(f"{key}: {value}\n")


if __name__ == "__main__":
    # Check for help command
    command = (
        input("Enter a command (-help or /help for instructions): ").strip().lower()
    )
    if command in ["-help", "/help"]:
        show_help()

    # Prompt user for city and units
    city = input("Select the location desired: ").strip()
    unit = input("Select your desired unit (standard, metric or imperial): ").lower()
    while unit not in ["standard", "metric", "imperial"]:
        unit = input(
            "Error selecting unit, try again (standard, metric or imperial): "
        ).lower()

    # Prompt user for export format
    export_format = input(
        "Select export format (csv, json or txt) or press Enter to skip: "
    ).lower()
    while export_format not in ["", "csv", "json", "txt"]:
        export_format = input(
    "Invalid format. Select export format (csv, json or txt) or press Enter to skip: "
        ).lower()

    # Fetch the weather data
    weather_data = fetch_weather_data(city, unit)
    if weather_data:
        # Process and export weather data
        temp = weather_data["main"]["temp"]
        feels_like = weather_data["main"]["feels_like"]
        wind_speed = weather_data["wind"]["speed"]
        humidity = weather_data["main"]["humidity"]
        description = weather_data["weather"][0]["description"]
        sunrise_time = dt.datetime.fromtimestamp(weather_data["sys"]["sunrise"], dt.UTC)
        sunset_time = dt.datetime.fromtimestamp(weather_data["sys"]["sunset"], dt.UTC)

        # Prepare data for export
        weather_info = {
            "city": city,
            "temperature": f"{temp:.2f}",
            "feels_like": f"{feels_like:.2f}",
            "humidity": humidity,
            "wind_speed": wind_speed,
            "description": description,
            "sunrise": str(sunrise_time),
            "sunset": str(sunset_time),
        }

        # Add temperature unit
        if unit == "standard":
            weather_info["temp_unit"] = "K"
        elif unit == "metric":
            weather_info["temp_unit"] = "C"
        else:
            weather_info["temp_unit"] = "F"

        # Check if the user pressed Enter to skip the export
        if export_format:
            # Export data if a valid format is provided
            filename = f"weather_data_{city}.{export_format}"
            if export_format == "csv":
                export_to_csv(weather_info, filename)
            elif export_format == "json":
                export_to_json(weather_info, filename)
            else:
                export_to_txt(weather_info, filename)
            print(f"Weather data has been exported to {filename}")
        else:
            print("Export skipped.")

        # Console output
        print(f"Temperature in {city}: {temp:.2f}°{weather_info['temp_unit']}")
        print(
            f"Temperature in {city} feels like: "
            f"{feels_like:.2f}°{weather_info['temp_unit']}"
        )
        print(f"Humidity in {city}: {humidity}%")
        print(f"Wind speed in {city}: {wind_speed}m/s")
        print(f"General weather in {city}: {description}")
        print(f"Sun rises in {city} at {sunrise_time} local time")
        print(f"Sun sets in {city} at {sunset_time} local time")
