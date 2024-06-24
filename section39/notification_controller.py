import os
from dotenv import load_dotenv
from twilio.rest import Client

from data_model import DataModel

load_dotenv()
class NotificationController:

  def __init__(self, data_model):
    self.model: DataModel = data_model
    self.twilio_id: str = os.environ.get('TWILIO_ID')
    self.twilio_auth_token: str = os.environ.get('TWILIO_AUTH_TOKEN')
    self.twilio_virtual_number: str = os.environ.get('TWILIO_VIRTUAL_NUMBER')
    self.twilio_verified_number: str = os.environ.get('TWILIO_VERIFIED_NUMBER')

  # build function to send twilio sms
  def send_sms(self, body: str) -> None:
    client = Client(self.twilio_id, self.twilio_auth_token)
    message = client.messages.create(
      from_=self.twilio_virtual_number,
      body=body,
      to=self.twilio_verified_number
    )

  # build function to fetch flight match & send sms per match