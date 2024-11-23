import requests
import json

with open("config.json", "r") as file:
    config = json.load(file)

API_KEY = config["API_KEY"]

WEATHER_BASE_URL = "https://api.openweathermap.org/data/2.5/onecall"

def get_weather_data(lat, lon):
    try:
        params = {
            "lat": lat,
            "lon": lon,
            "exclude": "minutely,hourly,alerts",
            "appid": API_KEY,
            "units": "metric"  # Use 'imperial' for Fahrenheit
        }
        response = requests.get(WEATHER_BASE_URL, params=params)
        response.raise_for_status()
        return response.json()

    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")
        return None


GEOCODING_URL = "http://api.openweathermap.org/geo/1.0/direct"

def get_city_coordinates(city):
    try:
        params = {
            "q": city,
            "limit": 1,
            "appid": API_KEY
        }
        response = requests.get(GEOCODING_URL, params=params)
        response.raise_for_status()
        data = response.json()
        if data:
            return data[0]["lat"], data[0]["lon"]
        else:
            print("City not found.")
            return None, None
    except requests.exceptions.RequestException as e:
        print(f"Error fetching city coordinates: {e}")
        return None, None
