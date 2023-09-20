import requests
from twilio.rest import Client


TWILIO_ACCOUNT_SID = "XXXX"
TWILIO_AUTH_TOKEN = "####"
SMS_NUMBER = +1234
OWM_ENDPOINT = "https://api.openweathermap.org/data/2.8/onecall"
api_key = "####"
weather_parameters = {
        "lat": -1234,
        "lon": -1234,
        "exclude": "current,minutely,daily",
        "appid": api_key
    }
account_sid = TWILIO_ACCOUNT_SID
auth_token = TWILIO_AUTH_TOKEN

response = requests.get(url=OWM_ENDPOINT, params=weather_parameters)
response.raise_for_status()
weather_data = response.json()
weather_forcast = weather_data['hourly'][0:12]

will_rain = False
for hour_data in weather_forcast:
    condition_code = hour_data['weather'][0]['id']
    print(condition_code)
    if condition_code < 690:
        will_rain = True

if will_rain:
    print("rain")
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
            body="Es wird heute regnen. Denk daran, einen Regenschirm mitzunehmen ☔.",
            from_='+1234',
            to='+4567'
        )

    print(message.status)
