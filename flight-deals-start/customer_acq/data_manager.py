import requests
import pprint
from flight_search import FlightSearch

SHEETY_URL = "https://api.sheety.co/b3e23f917dcbc032b319d52cb90c0b39/flightDealProject/prices"

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.destination_data = {}
    
    
    def get_destination_data(self):
        content = requests.get(SHEETY_URL)
        data = content.json()
        #pprint(data)
        self.destination_data = data["prices"]
        return self.destination_data


    def update_destination_codes(self):
        flight_code = FlightSearch()
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": flight_code.get_destination_code(city['city'])
                }
            }
            # Update google sheety file
            response = requests.put(
                url=f"{SHEETY_URL}/{city['id']}",
                json=new_data
            )
            print(response.text)


    
    
