import os
import requests

from section40.data_model import DataModel


class UserController:

  def __init__(self, data_model: DataModel):
    self.model: DataModel = data_model

    self.SHEETY_API_KEY: str = os.environ.get('SHEETY_API_KEY')
    self.SHEETY_TOKEN: str = os.environ.get('SHEETY_TOKEN')
    self.sheety_headers: dict[str, str] = {
      'Authorization': f'Basic {self.SHEETY_TOKEN}'
    }

    self.sheety_endpoint: str = f'https://api.sheety.co/{self.SHEETY_API_KEY}/flights/users'

  def validate_user_email(self, initial_email_input: str, second_email_input: str):
    if initial_email_input != second_email_input:
      raise Exception(
        f"Emails do not match! Initial email input: {initial_email_input}, Second email input: {second_email_input}"
      )
