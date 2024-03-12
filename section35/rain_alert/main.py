import requests

owm_endpoint = "https://api.openweathermap.org/data/2.5/forecast"

api_key = "82a5bd518c48cfee0874b684b5c86dca"

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
  print("Bring an umbrella.")