import requests
from twilio.rest import Client

API_KEY = "Your API Key"
account_sid = "Your Acount sid"
auth_token = "Your Auth Token"
lat = 48.546
lon = -114.302

weather_params = {
    "lat": lat,
    "lon": lon,
    "appid": API_KEY,
    "exclude": "current,minutely,daily"
}

URL = f"https://api.openweathermap.org/data/2.5/onecall"

will_rain = False

def check_for_rain(arr):
    for condition in arr:
        if (condition < 700):
            will_rain = True
            return will_rain
        else:
            return will_rain

response = requests.get(URL, params=weather_params)
response.raise_for_status()
weather_data = response.json()
next_12_hours = weather_data["hourly"][:12]
codes = [next_12_hours[i]["weather"][0]["id"] for i in range(len(next_12_hours))]

if check_for_rain(codes):
    client = Client(account_sid, 
            auth_token)

    message = client.messages.create(
            body="It's is going to rain today. Remember to bring an ☔.",
            from_='+19783557154',
            to='Your Phone Number'
        )
    print(message.status)
