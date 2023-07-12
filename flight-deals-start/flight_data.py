from datetime import datetime, timedelta
import cred

TEQUILLA_URL = "https://tequila-api.kiwi.com"
TEQUILLA_API = cred.TEQUILA_API_KEY

tomorrow_date = datetime.now() + timedelta(hours=24)
tomorrow_date_frt = tomorrow_date.strftime("%d/%m/%Y")

end_duration = tomorrow_date + timedelta(days=180)
end_duration_frt = end_duration.strftime("%d/%m/%Y")

class FlightData:
    #This class is responsible for structuring the flight data.
    def __init__(self, price, origin_city, origin_airport, destination_city, destination_airport,flight_time, return_time) -> None:
        self.price = price
        self.origin_city = origin_city
        self.origin_airport = origin_airport
        self.destination_city = destination_city
        self.destination_airport = destination_airport
        self.flight_time = flight_time
        self.return_time = return_time
