import requests
from datetime import datetime

MY_LAT = 51.507351
MY_LON = -0.127758

#
# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# # response.raise_for_status() - raises an exception of status is not 200
# # response.status_code - returns the status call of the API
# # response.json() - returns the response in JSON format
# # response.json()['iss_position] - returns a specific object from the response
#
# data = response.json()
#
# longitude = data["iss_position"]["longitude"]
# latitude = data["iss_position"]["latitude"]
#
# iss_position = (longitude, latitude)
#
# print(iss_position)

parameters = {
  'lat': MY_LAT,
  'lng': MY_LON,
  'formatted': 0
}

# params - append parameters to the URL for get requests
response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()

sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]

# split date and time
formatted_sunrise = sunrise.split("T")
formatted_sunset = sunset.split("T")

print(formatted_sunrise, formatted_sunset)