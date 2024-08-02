# capstone 1. find amazing flight deals
## extra challenge - build using OOP with types
## step 1. set up a google sheet with price cut offs and the locations we want to go to
## step 2. match google sheet data with current flight deals
## step 3. send sns on flight deal matches

# capstone 2. build a flight club app for others to find flight deals
## based off https://jacksflightclub.com/ca
## extra challenge - build user creation programmatically (instead of through google forms), also add helpful comments for each method / class
import datetime

from flight_controller import FlightController
from data_model import DataModel, flight_search_criteria_type
from notification_controller import NotificationController
from user_controller import UserController

data_model = DataModel()
notifications = NotificationController(data_model)
flights = FlightController(data_model)
users = UserController(data_model)

flight_search_criteria: flight_search_criteria_type | list = []
original_location_code: str = 'YYC'
adults: int = 1
currency: str = 'CAD'
non_stop: str = 'true'
departure_date_six_months: datetime = datetime.datetime.now() + datetime.timedelta(days=1) + datetime.timedelta(days=6 * 30)

# comment user lines out to disable user creation
# users.create_user()
# users.fetch_users()
flights.fetch_flight_thresholds()

# # print(data_model.get_flight_thresholds())
flights.populate_flight_search_criteria(
  flight_search_criteria,
  original_location_code,
  adults,
  currency,
  non_stop,
  departure_date_six_months
)
flights.retrieve_available_flights()
# notifications.send_flight_matches_sms()
