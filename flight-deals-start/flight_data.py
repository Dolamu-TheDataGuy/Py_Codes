from datetime import datetime, timedelta

TEQUILLA_URL = "https://tequila-api.kiwi.com"

class FlightData:
    #This class is responsible for structuring the flight data.
    def __init__(self, price, departure_code, departure_city) -> None:
        self.price = price
        self.departure_code = departure_code
        self.departure_city  = departure_city
    

