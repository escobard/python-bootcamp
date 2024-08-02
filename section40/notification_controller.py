import os
from dotenv import load_dotenv
from twilio.rest import Client

from data_model import DataModel

load_dotenv()


class NotificationController:
  """
  The NotificationController class is responsible for managing notifications,
  specifically sending SMS messages using the Twilio API based on flight matches.
  """

  def __init__(self, data_model: DataModel):
    """
    Initializes the NotificationController with the provided DataModel instance
    and sets up necessary Twilio credentials.

    Args:
        data_model (DataModel): An instance of the DataModel class.
    """
    self.model: DataModel = data_model
    self.twilio_id: str = os.environ.get('TWILIO_ID')
    self.twilio_auth_token: str = os.environ.get('TWILIO_AUTH_TOKEN')
    self.twilio_virtual_number: str = os.environ.get('TWILIO_VIRTUAL_NUMBER')
    self.twilio_verified_number: str = os.environ.get('TWILIO_VERIFIED_NUMBER')

  def send_sms(self, body: str) -> None:
    """
    Sends an SMS message using the Twilio API.

    Args:
        body (str): The body of the SMS message to be sent.
    """
    client = Client(self.twilio_id, self.twilio_auth_token)
    message = client.messages.create(
      from_=self.twilio_virtual_number,
      body=body,
      to=self.twilio_verified_number
    )

  def send_flight_matches_sms(self) -> None:
    """
    Fetches flight matches from the DataModel and sends an SMS for each match.
    """
    for flight_match in self.model.get_flight_matches():
      sms_body: str = f"Low price alert! Only ${flight_match['price']} CAD to fly from {flight_match['origin_airport']} to {flight_match['destination_airport']}, on {flight_match['out_date']}."
      print(sms_body)
      self.send_sms(sms_body)