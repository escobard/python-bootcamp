import os
from dotenv import load_dotenv

load_dotenv()
class NotificationController:

  def __init__(self):
    self.twilio_id: str = os.environ.get('TWILIO_ID')
    self.twilio_auth_token: str = os.environ.get('TWILIO_AUTH_TOKEN')
    self.twilio_virtual_number: str = os.environ.get('TWILIO_VIRTUAL_NUMBER')
    self.twilio_verified_number: str = os.environ.get('TWILIO_VERIFIED_NUMBER')


  # build function to send twilio sms
  # build function to fetch flight match & send sms per match