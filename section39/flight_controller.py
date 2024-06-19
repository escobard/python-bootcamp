import os
import requests
from dotenv import load_dotenv

from data_model import DataModel

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
    print(sheety_request.text)
    self.model.set_flight_thresholds(sheety_request.json())

  def fetch_amadeus_jwt(self):
    amadeus_auth_request = requests.post(
      url=self.amadeus_auth_url,
      data=self.amadeus_auth_body,
      headers=self.amadeus_auth_headers
    )
    amadeus_auth_token: dict[str, str] = {
      'Authorization': f'Bearer {amadeus_auth_request.json()['access_token']}'
    }
    return amadeus_auth_token
