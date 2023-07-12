import requests
from data_manager import DataManager
import cred

TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"
TEQUILA_API_KEY = cred.TEQUILA_API_KEY

data_manager = DataManager()
sheet_data = data_manager.get_destination_data()


class FlightSearch:

    def get_destination_code(self, city_name):
        # Return "TESTING" for now to make sure Sheety is working. Get TEQUILA API data later.
        location_endpoint = TEQUILA_ENDPOINT+"/locations/query"
        headers = {"apikey": TEQUILA_API_KEY}
        parameters = {"term": city_name, "location_types": "city"}
        response = requests.get(url=location_endpoint,headers=headers, params=parameters)
        result = response.json()['locations']
        code = result[0]['code']
        return code



flight = FlightSearch()
print(flight.get_destination_code('Berlin'))
