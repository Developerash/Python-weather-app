import requests
import json

# Get the OpenWeatherMap API key from your account settings.
api_key = "YOUR_API_KEY"

# Get the city name from the user.
city = input("Enter a city name: ")

# Make an HTTP request to the OpenWeatherMap API.
url = "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=" + api_key
response = requests.get(url)

# Check the response status code.
if response.status_code == 200:
    # The request was successful, so get the weather data.
    weather_data = json.loads(response.content)

    # Print the weather data.
    print("The weather in " + city + " is:")
    print("* Temperature: " + weather_data["main"]["temp"] + "°C")
    print("* Humidity: " + weather_data["main"]["humidity"] + "%")
    print("* Pressure: " + weather_data["main"]["pressure"] + " hPa")
else:
    # The request was not successful, so print an error message.
    print("Error: " + response.status_code)