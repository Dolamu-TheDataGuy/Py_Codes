#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch

data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
#print(sheet_data)


if sheet_data[0]["iataCode"] == "":
    flight_search = FlightSearch()
    for row in sheet_data:
        row["iataCode"] = flight_search.get_destination_code(row["city"])
    print(f"sheet data:\n {sheet_data}")

    #Update iata code with TESTING to the destination data
    data_manager.destination_data = sheet_data
    # make a PUT (edit) to sheety API
    data_manager.update_destination_codes()