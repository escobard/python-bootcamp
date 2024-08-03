import os
import requests
import datetime
import json

from dotenv import load_dotenv

from section40.data_model import DataModel

load_dotenv()

user_body_type = dict[str, dict[str, str]]

class UserController:
  """
  The UserController class is responsible for managing user-related operations,
  including validating user emails, fetching users from the Sheety API, and creating new users.
  """

  def __init__(self, data_model: DataModel):
    """
    Initializes the UserController with the provided DataModel instance and
    sets up necessary API keys and endpoints.

    Args:
        data_model (DataModel): An instance of the DataModel class.
    """
    self.model: DataModel = data_model

    self.SHEETY_API_KEY: str = os.environ.get('SHEETY_API_KEY')
    self.SHEETY_TOKEN: str = os.environ.get('SHEETY_TOKEN')
    self.sheety_headers: dict[str, str] = {
      'Authorization': f'Basic {self.SHEETY_TOKEN}',
      'Content-Type': 'application/json'
    }

    self.sheety_users_endpoint: str = f'https://api.sheety.co/{self.SHEETY_API_KEY}/flights/users'

  def fetch_users(self) -> None:
    """
    Fetches users from the Sheety API and updates the DataModel with the retrieved data.
    """
    sheety_request = requests.get(url=self.sheety_users_endpoint, headers=self.sheety_headers)
    self.model.set_users(sheety_request.json())

  def create_user(self) -> None:
    """
    Prompts the user for their first name, last name, and email, validates the email,
    and creates a new user in the Sheety API if the user does not already exist.
    """
    first_name: str = str(input('Enter your first name: '))
    last_name: str = str(input('Enter your last name: '))
    initial_email: str = str(input('Enter your email: '))
    validate_email: str = str(input('Enter your email again: '))

    if initial_email != validate_email:
      raise Exception("Emails do not match!")

    user_body: user_body_type = {
      'user': {
        'timestamp': str(datetime.datetime.now()),
        'firstName': first_name,
        'lastName': last_name,
        'email': validate_email
      }
    }

    json_body = json.dumps(user_body)

    self.fetch_users()

    users_list = self.model.get_users()['users']

    # https://stackoverflow.com/questions/46136665/how-to-check-if-value-exists-in-python-list-of-objects
    if [item for item in users_list if item['email'] == validate_email]:
      raise Exception('User already exists!')
    else:
      sheety_request = requests.post(url=self.sheety_users_endpoint, headers=self.sheety_headers, data=json_body)
      print(f'New user was created with:', sheety_request.json())