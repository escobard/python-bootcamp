# find amazing flight deals
## extra challenge - build using OOP
## step 1. set up a google sheet with price cut offs and the locations we want to go to
## step 2. match google sheet data with current flight deals
## step 3. send sns on flight deal matches

from flight_controller import FlightController
from data_model import DataModel

data_model = DataModel()
flights = FlightController(data_model)

flights.fetch_flight_thresholds()

print(data_model.get_flight_thresholds())
##print(flights.fetch_amadeus_jwt())
