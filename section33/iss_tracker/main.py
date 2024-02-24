import requests
import time
from datetime import datetime
import smtplib

MY_LAT = 51.507351  # Your latitude
MY_LONG = -0.127758  # Your longitude

email = "escobardtraining@gmail.com"
password = "tpsx mkhh gfpp zxnf"


def is_iss_overhead():
  response = requests.get(url="http://api.open-notify.org/iss-now.json")
  response.raise_for_status()
  data = response.json()

  iss_latitude = float(data["iss_position"]["latitude"])
  iss_longitude = float(data["iss_position"]["longitude"])

  # Your position is within +5 or -5 degrees of the ISS position.
  if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5:
    return True


def is_night():
  parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
  }

  response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
  response.raise_for_status()
  data = response.json()
  sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
  sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

  # returns the hour for current time
  time_now = datetime.now().hour

  if time_now >= sunset or time_now <= sunrise:
    return True


# If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.

while True:
    # run the loop to check ISS longitude / latitude match every 60 seconds
    time.sleep(60)
    if is_iss_overhead() and is_night():
      connection = smtplib.SMTP('smtp.gmail.com')
      connection.starttls()
      connection.login(email, password)
      connection.sendmail(from_addr=email, to_addrs=email, msg="Subject: Look Up☝️\n\n The ISS is above you in the sky")
