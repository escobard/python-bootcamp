import os
import requests
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

proxy_client = TwilioHttpClient()
proxy_client.session.proxies = {'https': os.environ['https_proxy']}

account_sid = "AC52978fa2d4d7e687a9503d47fb6e7dca"
auth_token = os.environ.get("AUTH_TOKEN")

owm_endpoint = "https://api.openweathermap.org/data/2.5/forecast"

# can export into env variables same way as with js - using export, then consuming env variable
## os.environ.get("") retrieves env value by key
api_key = os.environ.get("OWM_API_KEY")

parameters = {
  "lat": 51.0447,
  "lon": -0.127758,
  "appid": api_key,
  "cnt": 4
}

response = requests.get(url=owm_endpoint, params=parameters)

response.raise_for_status()
weather_data = response.json()
print(weather_data["list"][0]["weather"][0]["id"])


will_rain = False
for hour_data in weather_data["list"]:
  condition_code = hour_data["weather"][0]["id"]
  print(condition_code)
  # if weather api data has an id less than 700, there is a chance of rain
  if int(condition_code) < 700:
    will_rain = True

if will_rain:
  client = Client(account_sid, auth_token, http_client=proxy_client)
  message = client.messages.create(
    body="It's going to rain today. Remember to bring an umbrella ☔",
    from_='+12138954699',
    to='+14038284954'
  )
  print(message.status)