import os
import requests
import datetime
import json

from dotenv import load_dotenv

from section40.data_model import DataModel

load_dotenv()


class UserController:

  def __init__(self, data_model: DataModel):
    self.model: DataModel = data_model

    self.SHEETY_API_KEY: str = os.environ.get('SHEETY_API_KEY')
    self.SHEETY_TOKEN: str = os.environ.get('SHEETY_TOKEN')
    self.sheety_headers: dict[str, str] = {
      'Authorization': f'Basic {self.SHEETY_TOKEN}',
      'Content-Type': 'application/json'
    }

    self.sheety_users_endpoint: str = f'https://api.sheety.co/{self.SHEETY_API_KEY}/flights/users'

  def validate_user_email(self, initial_email_input: str, validate_email_input: str):
    if initial_email_input != validate_email_input:
      raise Exception("Emails do not match!")

  def get_users(self):
    sheety_request = requests.get(url=self.sheety_users_endpoint, headers=self.sheety_headers)
    # add exception for when results are null
    self.model.set_flight_thresholds(sheety_request.json())

  def post_user(self):
    first_name: str = str(input('Enter your first name: '))
    last_name: str = str(input('Enter your last name: '))
    initial_email: str = str(input('Enter your email: '))
    validate_email: str = str(input('Enter your email: '))

    self.validate_user_email(initial_email, validate_email)

    user_body: dict[str, dict[str, str]] = {
      'user': {
        'timestamp': str(datetime.datetime.now()),
        'firstName': first_name,
        'lastName': last_name,
        'email': validate_email
      }
    }

    json_body = json.dumps(user_body)

    ## TODO - add logic to fetch available users first

    ## TODO - add logic to send a put request to update a user if email already exists

    sheety_request = requests.post(url=self.sheety_users_endpoint, headers=self.sheety_headers, data=json_body)
    print(f'New user was created with:', sheety_request.json())
