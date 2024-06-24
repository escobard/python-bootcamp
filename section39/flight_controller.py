import os
import requests
import datetime
from dotenv import load_dotenv

from data_model import DataModel, flight_search_criteria_type, flight_matches_type

load_dotenv()

# TODO - add a comment explaining each method
# TODO - strengthen types
class FlightController:

  def __init__(self, data_model: DataModel):
    self.model: DataModel = data_model

    self.SHEETY_API_KEY: str = os.environ.get('SHEETY_API_KEY')
    self.SHEETY_TOKEN: str = os.environ.get('SHEETY_TOKEN')
    self.sheety_headers: dict[str, str] = {
      'Authorization': f'Basic {self.SHEETY_TOKEN}'
    }
    self.sheety_endpoint: str = f'https://api.sheety.co/{self.SHEETY_API_KEY}/flights/prices'

    self.AMADEUS_API_KEY: str = os.environ.get('AMADEUS_API_KEY')
    self.AMADEUS_API_SECRET: str = os.environ.get('AMADEUS_API_SECRET')

    self.amadeus_auth_url: str = 'https://test.api.amadeus.com/v1/security/oauth2/token'
    self.amadeus_auth_headers: dict[str, str] = {
      'Content-Type': 'application/x-www-form-urlencoded'
    }
    self.amadeus_auth_body: dict[str, str] = {
      'grant_type': 'client_credentials',
      'client_id': self.AMADEUS_API_KEY,
      'client_secret': self.AMADEUS_API_SECRET
    }

    self.amadeus_flight_search_url: str = 'https://test.api.amadeus.com/v2/shopping/flight-offers'

  def fetch_flight_thresholds(self) -> None:
    sheety_request = requests.get(url=self.sheety_endpoint, headers=self.sheety_headers)
    # add exception for when results are null
    self.model.set_flight_thresholds(sheety_request.json())

  def fetch_amadeus_jwt(self) -> dict[str, str]:
    amadeus_auth_request = requests.post(
      url=self.amadeus_auth_url,
      data=self.amadeus_auth_body,
      headers=self.amadeus_auth_headers
    )
    amadeus_auth_token: dict[str, str] = {
      'Authorization': f'Bearer {amadeus_auth_request.json()['access_token']}'
    }
    return amadeus_auth_token

  # TODO - pass in search criteria as arguments
  def populate_flight_search_criteria(self):
    if self.model.get_flight_thresholds() is None:
      raise Exception('No flight thresholds defined')
    else:
      flight_search_criteria: flight_search_criteria_type | list = []
      original_location_code: str = 'YYC'
      adults: int = 1
      currency: str = 'CAD'
      non_stop: str = 'true'
      departure_date_six_months = datetime.datetime.now() + datetime.timedelta(days=1) + datetime.timedelta(days=6 * 30)

      # try to convert to list comprehension in part 2
      for flight_threshold in self.model.get_flight_thresholds()['prices']:
        flight_search_criteria.append({
          'originLocationCode': original_location_code,
          'destinationLocationCode': flight_threshold['iataCode'],
          'departureDate': departure_date_six_months.strftime('%Y-%m-%d'),
          'adults': adults,
          'currencyCode': currency,
          'nonStop': non_stop,
          'maxPrice': flight_threshold['lowestPrice']
        })

      self.model.set_flight_search_criteria(flight_search_criteria)

  # build method to send GET requests to AMADEUS for each flight_search_criteria
  def retrieve_available_flights(self):
    self.populate_flight_search_criteria()
    jwt_headers = self.fetch_amadeus_jwt()
    flight_search_criteria_list = self.model.get_flight_search_criteria()
    flight_matches: flight_matches_type | list = []

    for flight_search_criteria in flight_search_criteria_list:
      amadeus_available_flights_request = requests.get(
        url=self.amadeus_flight_search_url,
        params=flight_search_criteria,
        headers=jwt_headers
      )

      if amadeus_available_flights_request.json()['data']:
        print(
          f"Flights found for {flight_search_criteria['originLocationCode']} to {flight_search_criteria['destinationLocationCode']}")
        for flight_match in amadeus_available_flights_request.json()['data']:
          flight_match = {
            'price': flight_match['price']['total'],
            'origin_airport': flight_search_criteria['originLocationCode'],
            'destination_airport': flight_search_criteria['destinationLocationCode'],
            'out_date': flight_match['itineraries'][0]['segments'][0]['departure']['at']
          }

          flight_matches.append(flight_match)
      else:
        print(
          f"Flights not found for {flight_search_criteria['originLocationCode']} to {flight_search_criteria['destinationLocationCode']}")

    self.model.set_flight_matches(flight_matches)
