from dotenv import load_dotenv
import os
from django.shortcuts import render
import requests

load_dotenv()

"""
    This module contains the views for our weather app.
    It handles the GET and POST requests for the home page.
    It displays the weather details of a city which is entered by the user in the search bar.
    If the user does not enter a city, it defaults to 'Dubai'.
    It uses the OpenWeatherMap API to get the weather details of the city.
    The API key is stored in the 'API_KEY' variable.
    The URL for the API is constructed using the city name and the API key.
    The 'params' dictionary is used to specify the units for the temperature.
    The API response is converted to a JSON object using the 'json()' method of the response object.
    The weather details are stored in the 'details' dictionary.
    The 'render' function is used to render the 'index.html' template with the 'details' dictionary.
    If there is an error in the API response, the 'exception_occurred' variable is set to True.
"""
def home(request):
    # API key for OpenWeatherMap
    API_KEY = os.getenv('API_KEY')
    print(f'API_KEY: {API_KEY}')

    # Get city name from form
    if 'city' in request.POST:
        city = request.POST['city']
    else:
        city = 'Dubai'

    # Get weather data from OpenWeatherMap API
    url=f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"
    params = {
        'units': 'Metric'
    }

    # Get weather data from OpenWeatherMap API
    response = requests.get(url,params=params).json()

    try:
        # Get weather data from OpenWeatherMap API
        details={
            'city':city,
            'description':response['weather'][0]['description'],
            'icon':response['weather'][0]['icon'],
            'temperature':response['main']['temp'],
            'humidity':response['main']['humidity'],
            'wind_speed':convert_wind_speed(response['wind']['speed'])
        }

        # Render template with weather data
        return render(request,'index.html',{'details':details})
    
    except (KeyError, IndexError):
        # Exception occurred
        exception_occurred = True

        # Render template with error message
        return render(request,'index.html',{'exception_occurred':exception_occurred})

"""
    This function converts the wind speed from meters per second (m/s) to kilometers
    per hour (km/h).

    Parameters:
    - wind_speed (float): The wind speed in meters per second.

    Returns:
    - float: The wind speed in kilometers per hour.
"""
def convert_wind_speed(wind_speed):
    # Convert wind speed from m/s to km/h
    return wind_speed * 3.6