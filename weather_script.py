import requests

def get_weather(city_name):
    """
    Fetches weather data for a given city in Argentina from OpenWeatherMap API.

    Args:
        city_name (str): Name of the city.

    Returns:
        dict: Weather data if successful, or an error message.
    """
    api_key = "096fa1dbd29018f450074620c6d65fb9"  # Auth API key
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": f"{city_name},AR",  # AR is the country code for Argentina
        "appid": api_key,
        "units": "metric"  # Use metric units for temperature in Celsius
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx and 5xx)
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}

def main():
    print("Weather Information for Cities in Argentina")
    city_name = input("Enter the name of the city: ")

    weather_data = get_weather(city_name)

    if "error" in weather_data:
        print(f"Error fetching weather data: {weather_data['error']}")
    else:
        print(f"City: {weather_data['name']}")
        print(f"Temperature: {weather_data['main']['temp']}°C")
        print(f"Weather: {weather_data['weather'][0]['description'].capitalize()}")
        print(f"Humidity: {weather_data['main']['humidity']}%")
        print(f"Wind Speed: {weather_data['wind']['speed']} m/s")

if __name__ == "__main__":
    main()