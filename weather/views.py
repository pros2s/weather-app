import  requests
from django.shortcuts import render

def index(request):
    appid = '43548db585f5bc3f3b0a61a05d64301b'
    url = 'https://api.openweathermap.org/data/2.5' \
          '/weather?q={' \
          '}&units=metric&appid=' + appid

    city = 'London'
    res = requests.get(url.format(city)).json()

    city_info = {
        'city': city,
        'temp': res["main"]["temp"],
        'icon': res["weather"][0]["icon"],
        'wind': res["wind"]["speed"]
    }

    context = {
        'info': city_info
    }
    return render(request, 'weather/index.html', context)