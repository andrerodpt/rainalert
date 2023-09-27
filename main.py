import requests
from credentials import API_KEY
from telegram import Telegram


API_URL = 'https://api.openweathermap.org/data/2.5/onecall'
PARAMETERS = {
    'lat': 38.695894,
    # 'lat': 17.55,
    'lon': -9.159886,
    # 'lon': -51.95,
    'exclude': 'current,minutely,daily',
    'appid': API_KEY
}

response = requests.get(url=API_URL, params=PARAMETERS)
response.raise_for_status()
weather_data = response.json()

twelve_hour_forecast = weather_data['hourly'][:12]

bring_an_umbrella = False
for hour in twelve_hour_forecast:
    if hour['weather'][0]['id'] < 700:
        bring_an_umbrella = True

if bring_an_umbrella:
    telegram_bot = Telegram()
    send_message_return = telegram_bot.send_message('Please bring an umbrella.')

