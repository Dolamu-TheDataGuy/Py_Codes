#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager
from datetime import datetime, timedelta
import json

ORIGIN_CITY = "LDN"


data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
# print(sheet_data)


if sheet_data[0]["iataCode"] != "":
    city_names = [row["city"] for row in sheet_data]
    print(city_names)
    flight_search = FlightSearch()
    for row in sheet_data:
        row["iataCode"] = flight_search.get_destination_code(row["city"])
    #print(f"sheet data:\n {sheet_data}")

    #Update iata code with TESTING to the destination data
    data_manager.destination_data = sheet_data
    # make a PUT (edit) to sheety API
    data_manager.update_destination_codes()
    with open("sheet.json", "w") as f:
        json.dump(sheet_data, f, indent=4)

today = datetime.now() + timedelta(1)
six_month_from_today = datetime.now() + timedelta(6*30)

for destination in sheet_data:
    flight = FlightSearch().research_flight(
        ORIGIN_CITY,
        destination["iataCode"],
        today,
        six_month_from_today
    )
    
if flight.prices < destination["lowestPrice"]:
    NotificationManager().send_notification(
        message=f"Low price alert! only ${flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}"
    )

