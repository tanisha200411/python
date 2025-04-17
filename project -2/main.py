import requests
from dotenv import load_dotenv
import os

load_dotenv()

def get_weather(city, api_key):
    weather_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,

        # temperature in Celsius
        "units": "metric"  
    }
    try:
        response = requests.get(weather_url, params=params)
        # check if the request is successful
        response.raise_for_status() 
        data = response.json()  
        return {
            "city": data["name"],
            "temperature": data["main"]["temp"],
            "description": data["weather"][0]["description"]
        }
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}

def main():
    api_key = os.getenv("API_KEY") 
    if not api_key:
        print("Error: API key not found. Please check your .env file.")
        return
    
    city = input("Enter the city name: ")
    weather = get_weather(city, api_key)
    
    if "error" in weather:
        print(f"Error: {weather['error']}")
    else:
        print(f"Weather in {weather['city']}:")
        print(f"Temperature: {weather['temperature']}°C")
        print(f"Description: {weather['description']}")

if __name__ == "__main__":
    main()
