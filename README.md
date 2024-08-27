# Weather Fetching Program

## Description

This Weather Fetching Program is a command-line application that retrieves weather data from the OpenWeatherMap API for a specified city. It allows users to choose the temperature unit and export format for the weather data.

## Features

- Fetch current weather data for any city
- Choose between standard (Kelvin), metric (Celsius), or imperial (Fahrenheit) units
- Export data in CSV, JSON, or TXT format
- Display weather information in the console
- Error handling for API requests
- Help command for usage instructions

## Installation

### Option 1: Using the Release ZIP (Recommended for non-developers)

1. Download the latest release ZIP file from the GitHub [releases](https://github.com/sktn00/git-weathered/releases) page.
2. Extract the ZIP file to your desired location.
3. Open the `api_key.txt` file and replace its contents with your OpenWeatherMap API key.

### Option 2: Cloning the Repository (For developers)

1. Clone this repository:
`git clone https://github.com/sktn00/git-weathered.git`

2. Navigate to the project directory:
`cd git-weathered/`

3. Install the required dependencies:
`pip install requirements.txt`

4. Create an `api_key.txt` file in the project root and add your OpenWeatherMap API key to it.

## Usage

### Using the Executable (from Release ZIP)

1. Open a terminal or command prompt.
2. Navigate to the directory containing the extracted files.
3. Run the program:
- On Unix-like systems (Linux, macOS):
  ```
  ./main
  ```
- On Windows:
  ```
  main.exe
  ```

### Running the Python Script (for developers)
`python main.py`

### Automated Bash Script

The repository includes an automated bash script that installs dependencies and runs the program with default parameters. To use it:

1. Make the script executable:
`chmod +x run_weather.sh`
2. Run the script:
`./run_weather.sh`

## Program Flow

1. The program will prompt you to enter a command or press Enter to continue.
2. Enter the name of the city for which you want weather data.
3. Choose the temperature unit (standard, metric, or imperial).
4. Select the export format (csv, json, txt) or press Enter to skip exporting.
5. The program will display the weather information in the console.
6. If an export format was selected, the data will be saved to a file in the chosen format.

## Help Command

To view usage instructions, run the program and enter `-help` or `/help` when prompted for a command.

## API Key

This program requires an API key from OpenWeatherMap. If you don't have one:

1. Sign up at [OpenWeatherMap](https://openweathermap.org/api)
2. Generate an API key
3. Add the key to the `api_key.txt` file

## Error Handling

The program includes error handling for various API-related issues, including:

- Bad requests
- Unauthorized access (invalid API key)
- Rate limiting
- Network connection problems

If an error occurs, an appropriate message will be displayed.

## Contributing

Contributions to this project are welcome. Please fork the repository and submit a pull request with your changes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [OpenWeatherMap](https://openweathermap.org/) for providing the weather data API