import requests
from datetime import datetime

MY_LAT = 51.507351
MY_LONG = -0.127758

parameters = {
    "lat": MY_LAT,
    "long": MY_LONG,
    "formatted": 0,
}


#response = requests.get(f"https://api.sunrise-sunset.org/json?lat={MY_LAT}&lng={MY_LONG}")

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)

response.raise_for_status()

data = response.json()
sunrise = data['results']['sunrise'].split("T")[1].split(":")[0]
sunset = data['results']['sunset'].split("T")[1].split(":")[0]

info = (sunrise, sunset)

print(info)

time_now = datetime.now()
print(time_now.hour)

