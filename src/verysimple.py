# This Python script helps in fetching weather by connecting to weather API based on the location (its unfinished)
import requests

def get_weather_by_city(city_name):
    # 1 Geocoding API: Convert city name to Latitude and Longitude
    geocode_url = f"https://open-meteo.com{city_name}&count=1&language=en&format=json"
    geo_response = requests.get(geocode_url).json()

    if not geo_response.get("results"):
        return f"Error: City '{city_name}' not found."

    location_data = geo_response["results"][0]
    lat = location_data["latitude"]
    lon = location_data["longitude"]
    country = location_data.get("country", "Unknown")

    # 2 Weather Forecast API: Fetch live parameters
    weather_url = f"https://open-meteo.com{lat}&longitude={lon}&current_weather=true"
    weather_response = requests.get(weather_url).json()

    current = weather_response.get("current_weather")
    if not current:
        return "Error: Could not retrieve weather data."

    return {
        "Location": f"{location_data['name']}, {country}",
        "Temperature": f"{current['temperature']}°C",
        "Wind Speed": f"{current['windspeed']} km/h",
        "Weather Code": current['weathercode']
    }

# Example Usag
#user_input = input("Enter a city name: ")
#weather_info = get_weather_by_city(user_input)

#if isinstance(weather_info, dict):
 #   print(f"\nWeather info for {weather_info['Location']}:")
  #  print(f"- Temperature: {weather_info['Temperature']}")
   # print(f"- Wind Speed: {weather_info['Wind Speed']}")
#else:
    #print(weather_info)
