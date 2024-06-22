import os
import requests
import datetime
from dotenv import load_dotenv

from data_model import DataModel, flight_search_criteria_type

load_dotenv()


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

  def fetch_flight_thresholds(self) -> None:
    sheety_request = requests.get(url=self.sheety_endpoint, headers=self.sheety_headers)
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

  # rebuild to build a list of query parameters for GET
  def populate_flight_search_criteria(self):
    if self.model.get_flight_thresholds() is None:
      raise Exception('No flight thresholds defined')
    else:
      flight_search_criteria: flight_search_criteria_type | list = []
      original_location_code: str = 'YYC'
      adults: int = 1
      departure_date_tomorrow = datetime.datetime.now() + datetime.timedelta(days=1)
      departure_date_six_months = departure_date_tomorrow + datetime.timedelta(days=6*30)
      print(departure_date_six_months.strftime('%Y-%m-%d'))

      # try to convert to list comprehension in part 2
      for flight_threshold in self.model.get_flight_thresholds()['prices']:
        flight_search_criteria.append({
          'originLocationCode': original_location_code,
          'destinationLocationCode': flight_threshold['iataCode'],
          'departureDate': departure_date_six_months,
          'adults': adults,
          'maxPrice': flight_threshold['lowestPrice']
        })

      self.model.set_flight_search_thresholds(flight_search_criteria)

  # build method to send GET requests to AMADEUS for each flight_search_criteria
