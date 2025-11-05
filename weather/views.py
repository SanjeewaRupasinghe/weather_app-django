from django.http import HttpResponse
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
        'units': 'metric'
    }

    response = requests.get(url,params=params).json()

    print(response)

    description = response['weather'][0]['description']
    temperature = response['main']['temp']
    humidity = response['main']['humidity']
    wind_speed = response['wind']['speed']

    return render(request,'index.html',{'description':description,'temperature':temperature,'humidity':humidity,'wind_speed':wind_speed})



# 99f4d251142c2387b38ce64a1496525c