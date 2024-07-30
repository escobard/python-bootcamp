import os
import requests
import datetime
from dotenv import load_dotenv

from section40.data_model import DataModel

load_dotenv()


class UserController:

  def __init__(self, data_model: DataModel):

    self.SHEETY_API_KEY: str = os.environ.get('SHEETY_API_KEY')
    self.SHEETY_TOKEN: str = os.environ.get('SHEETY_TOKEN')
    self.sheety_headers: dict[str, str] = {
      'Authorization': f'Basic {self.SHEETY_TOKEN}'
    }

    self.sheety_endpoint: str = f'https://api.sheety.co/{self.SHEETY_API_KEY}/flights/users'

  def validate_user_email(self, initial_email_input: str, validate_email_input: str):
    if initial_email_input != validate_email_input:
      raise Exception("Emails do not match!")

  def get_users(self):
    print()

  def post_user(self):
    first_name: str = str(input('Enter your first name: '))
    last_name: str = str(input('Enter your last name: '))
    initial_email: str = str(input('Enter your email: '))
    validate_email: str = str(input('Enter your email: '))

    self.validate_user_email(initial_email, validate_email)

    user_body: dict[str, dict[str, str]] = {
      'users': {
        'Timestamp': datetime.datetime.now(),
        'First Name': first_name,
        'Last Name': last_name,
        'Email': validate_email
      }
    }

    requests.post(url=self.sheety_endpoint, headers=self.sheety_headers, data=user_body)
    print(f'New user was created with First name: {user_body['users']['First Name']}, Last name: {user_body['users']['Last Name']} and Email: {user_body['users']['Email']}')
