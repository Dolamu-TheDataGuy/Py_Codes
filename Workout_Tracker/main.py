import requests
import credential
from datetime import datetime
import json

exercise_url: str = "https://trackapi.nutritionix.com/v2/natural/exercise"
google_sheet_url: str = "https://api.sheety.co/b3e23f917dcbc032b319d52cb90c0b39/myWorkoutData/workouts"

GENDER = "male"
WEIGHT_KG = "77"
HEIGHT_CM = "181"
AGE = "30"

exercise_input: str = input("Tell which exercise you did today? ")

# Authentication data, so API gives user access.
headers = {
    "x-app-id": credential.API_ID,
    "x-app-key": credential.API_KEY,
    "Content-Type": "application/json"
}

# Data to be uploaded to API base
parameters = {
    'query': exercise_input,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE,
}

response = requests.post(exercise_url, json=parameters, headers=headers)
result = response.json()
with open("text.json", "w") as f:
    json.dump(result, f, indent=4)

today_date = datetime.now().strftime("%Y/%m/%d")
current_time = datetime.now().strftime("%X")

for content in result["exercises"]:
    sheet_content = {
        "workout": {
            "date": today_date,
            "time": current_time,
            "exercise": content["name"].title(),
            "duration": content["duration_min"],
            "calories": content["nf_calories"]

        }
    }
    # Basic Authorization for sheety
    headers = {
        "Authorization": "Basic RG9sYW11OlBva2FodW50ZXJAOQ=="
    }

    sheet_response = requests.post(google_sheet_url, json=sheet_content, headers=headers)
    print(sheet_response.text)
