from django.shortcuts import render
import requests


def home(request):
    API_KEY = "99f4d251142c2387b38ce64a1496525c"

    if 'city' in request.POST:
        city = request.POST['city']
    else:
        city = 'Dubai'

    url=f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"
    params = {
        'units': 'Metric'
    }

    response = requests.get(url,params=params).json()

    try:
        
        details={
            'city':city,
            'description':response['weather'][0]['description'],
            'icon':response['weather'][0]['icon'],
            'temperature':response['main']['temp'],
            'humidity':response['main']['humidity'],
            'wind_speed':convert_wind_speed(response['wind']['speed'])
        }

        return render(request,'index.html',{'details':details})

    except (KeyError, IndexError):
        exception_occurred = True

        return render(request,'index.html',{'exception_occurred':exception_occurred})

"""
wind speed in m/s to km/h
"""
def convert_wind_speed(wind_speed):
    # Convert wind speed from m/s to km/h
    return wind_speed * 3.6
    
