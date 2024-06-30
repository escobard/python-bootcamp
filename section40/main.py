# capstone 1. find amazing flight deals
## extra challenge - build using OOP with types
## step 1. set up a google sheet with price cut offs and the locations we want to go to
## step 2. match google sheet data with current flight deals
## step 3. send sns on flight deal matches

# capstone 2. build a flight club app for others to find flight deals
## based off https://jacksflightclub.com/ca
## extra challenge - build user creation programmatically (instead of through google forms), also add helpful comments for each method / class

from flight_controller import FlightController
from data_model import DataModel
from notification_controller import NotificationController

data_model = DataModel()
notifications = NotificationController(data_model)
flights = FlightController(data_model)

flights.fetch_flight_thresholds()

# print(data_model.get_flight_thresholds())
flights.retrieve_available_flights()
notifications.send_flight_matches_sms()
