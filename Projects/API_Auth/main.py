import requests
import os
from datetime import datetime
from twilio.rest import Client

OWN_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"  # except key to remove parameters from url
api_key = os.environ.get("OWN_API_KEY")
account_sid = "AC0a6d75bed8596fe6d6c87d8406f622b1"
auth_token = os.environ.get("AUTH_TOKEN")

parameter = {
    "lat": 6.524379,
    "lon": 3.379206,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

response = requests.get(OWN_Endpoint, params=parameter)
print(response.status_code)
weather_data = response.json()
print(weather_data)
print(weather_data["hourly"][0]['weather'][0]["id"])

weather_slice = weather_data['hourly'][:12]

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data['weather'][0]['id']
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
            body="It would rain today, Please take your Umbrella☂️",
            from_ = "+17605238493",
            to = "+2348165539137"
        )

print(message.status)
