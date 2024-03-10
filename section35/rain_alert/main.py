import requests

api_key = "82a5bd518c48cfee0874b684b5c86dca"

parameters = {
  "lat": 51.0447,
  "lon": 114.0719,
  "appid": api_key
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/weather?", params=parameters)

response.raise_for_status()
weather_data = response.json()
print(weather_data)