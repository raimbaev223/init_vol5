import requests
import json
from datetime import datetime
from bs4 import BeautifulSoup


def get_weather(city):
    key = '80d0ef1fce9db7f5eb46fa8e2e442641'
    api = f'https://api.openweathermap.org/data/2.5/weather?q={city},kg&appid={key}&units=metric'

    response = requests.get(api).content

    data = json.loads(response)
    temp = data['main']['temp']
    feels_like = data['main']['feels_like']
    sunrise = datetime.fromtimestamp(data['sys']['sunrise'])
    sunset = datetime.fromtimestamp(data['sys']['sunset'])
    wind = data['wind']['speed']
    weather = {
        'temp': temp,
        'feels_like': feels_like,
        'sunrise': sunrise,
        'sunset': sunset,
        'wind': wind
    }
    return weather


def get_news():
    response = requests.get('https://kloop.kg').text

    soup = BeautifulSoup(response, 'html.parser')
    posts = soup.find_all('a', class_='elementor-post__thumbnail__link')
    links = []
    for p in posts:
        href = p.get('href')
        links.append(href)
    # print(links)
    return links


print(get_weather('osh'))