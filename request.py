import requests
from dotenv import load_dotenv
import os
from datetime import datetime

def get_weather(city):
    """Fetch weather data for a given city from OpenWeatherMap API."""
    load_dotenv()
    api_key = os.getenv('WEATHER_API_KEY')
    base_url = "http://api.openweathermap.org/data/2.5/weather"

    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"
    }

    try:
        response = requests.get(base_url, params=params)
        print(f"Status Code: {response.status_code}")

        if response.status_code == 200:
            return response.json()
        elif response.status_code == 404:
            print("City: {City} not found.")
            return None
        elif response.status_code == 401:
            print("Invalid API key.")
            return None
        else:
            print(f"Error: {response.status_code}")
            return None
        
    except requests.exceptions.ConnectionError:
        print("No internet connection or API is down.")
        return None
    except requests.exceptions.Timeout:
        print("Request timed out. Try again later.")
        return None
    except Exception as e:
        print(f"Something unexpected went wrong: {e}")
        return None
    
def weather_data(data):
    """Print weather data in a readable format."""
    print(f"City: {data['name']}")
    print(f"Temperature: {data['main']['temp']}°C")
    print(f"  Humidity:     {data['main']['humidity']}%")
    print(f"  Weather:      {data['weather'][0]['description']}")

def save_weather_data(data, filename="weather_data.json"):
    """Save weather data to a JSON file."""
    with open(filename, "a") as f:
        f.write(f"\n--- {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} ---\n")
        f.write(f"City: {data['name']}\n")
        f.write(f"Temperature: {data['main']['temp']}°C\n")
        f.write(f"  Humidity:     {data['main']['humidity']}%\n")
        f.write(f"  Weather:      {data['weather'][0]['description']}\n")
    print(f"\n Weather data saved to {filename}")



if __name__ == "__main__":
    print("\nWeather App")
    print(". Get weather for a city")
    city = input("Enter city name: ")
    data = get_weather(city)
    if data:
      weather_data(data)
      save_weather_data(data)