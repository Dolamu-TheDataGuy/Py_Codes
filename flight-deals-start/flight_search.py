import requests
import cred

TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"
TEQUILA_API_KEY = cred.TEQUILA_API_KEY

class FlightSearch:

    def get_destination_code(self, city_name):
        # get destination code from Tequilla search API
        location_endpoint = TEQUILA_ENDPOINT+"/locations/query"
        headers = {"apikey": TEQUILA_API_KEY}
        parameters = {"term": city_name, "location_types": "city"}
        response = requests.get(url=location_endpoint,headers=headers, params=parameters)
        result = response.json()['locations']
        code = result[0]['code']
        return code

