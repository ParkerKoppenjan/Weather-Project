import requests

def get_coordinates(city):
    url = f'https://nominatim.openstreetmap.org/search?q={city}&format=json'
    response = requests.get(url, headers={"User-Agent": "WeatherAppProject"})
    data = response.json()
    if data:
        return data[0]['lat'], data[0]['lon']

def get_weather(coordinates):
    lat, lon = coordinates
    url = f'https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true'
    response = requests.get(url)
    data = response.json()
    if data:
        current_weather = data['current_weather']
        temperature_celsius = current_weather['temperature']
        temperature_fahrenheit = temperature_celsius * 9 / 5 + 32
        windspeed_kmh = current_weather['windspeed']
        windspeed_mph = windspeed_kmh * 0.621371
        return {
            'temperature': temperature_fahrenheit,
            'windspeed': windspeed_mph
        }


def main():
    city = input("Enter City: ")
    coordinates = get_coordinates(city)
    print(coordinates)
    weather = get_weather(coordinates)
    print(str(weather['temperature'])+ " F")
    print(str(weather['windspeed']) + " mph")
    input("Press Enter to exit...")


main()
