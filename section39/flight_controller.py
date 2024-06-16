import os
import requests

from data_model import DataModel


class FlightController:

  def __init__(self, data_model: DataModel):
    self.model: DataModel = data_model

    self.SHEETY_API_KEY: str = os.environ.get('SHEETY_API_KEY')
    self.SHEETY_TOKEN: str = os.environ.get('SHEETY_TOKEN')
    self.sheety_headers: dict[str, str] = {
      'Authorization': f'Basic {self.SHEETY_TOKEN}'
    }
    self.sheety_endpoint: str = f'https://api.sheety.co/{self.SHEETY_API_KEY}/flights/prices'

  def fetch_flight_thresholds(self):
    sheety_request = requests.get(url=self.sheety_endpoint, headers=self.sheety_headers)
    print(sheety_request.text)
    self.model.set_flight_thresholds(sheety_request.json())
