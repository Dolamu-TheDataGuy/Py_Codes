import requests
import cred
import json
from datetime import datetime, timedelta

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
    

    def research_flight(self, origin_city_code, destination_city_code, from_time, end_time):
        headers = {"apikey": TEQUILA_API_KEY}
        parameter = {
            "fly_from": origin_city_code,
            "fly_to": destination_city_code,
            "date_from": from_time.strftime("%d/%m/%Y"),
            "date_to": end_time.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "USD"
        }

        response = requests.get(url=TEQUILA_ENDPOINT+"/v2/search",
                                headers=headers,
                                params=parameter,
                                )

        results = response.json()
        # save result in json file for proper accessibility
        with open("data.json", "w") as f:
            json.dump(results, f, indent=4)

        data = results["data"][0]


samp =  FlightSearch().research_flight("PAR","BEG", datetime.now()+timedelta(hours=24), datetime.now()+timedelta(days=180))
