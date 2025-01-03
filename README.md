# City Weather CLI

## Description
A simple Python command-line tool that retrieves current weather information for a given city using OpenStreetMap and Open-Meteo APIs.

## Features
- Get geographic coordinates for a city
- Retrieve current temperature (in Fahrenheit)
- Get current wind speed (in mph)

## Requirements
- Python 3.x
- `requests` library

## Installation
```bash
pip install requests
```

## Usage
```bash
python weather_app.py
```
Enter a city name when prompted to get its current weather details.

## APIs Used
- OpenStreetMap Nominatim (Geocoding)
- Open-Meteo Weather API
