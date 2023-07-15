import requests
import os
import cred


USER: str = cred.SHEETY_USER
BEARER: str = cred.BEARER
PROJECT: str = "flightDealProject"
SHEET: str = "users"

base_url: str = "https://api.sheety.co"

def post_new_row(first_name: str, last_name: str, email: str) -> None:
    endpoint_url:str = f"/{USER}/{PROJECT}/{SHEET}"
    url: str = base_url + endpoint_url

    headers = {
        "Authorization": BEARER,
        "Content-Type": "application/json",
    }

    body = {
        "user" : {
            "firstname": first_name,
            "lastname": last_name,
            "email": email,
        }
    }
    
    response = requests.post(url=url, headers=headers, json=body)
    response.raise_for_status()
    print(response.text)

