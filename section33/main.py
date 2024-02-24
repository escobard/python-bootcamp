import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")
# response.raise_for_status() - raises an exception of status is not 200
# response.status_code - returns the status call of the API
# response.json() - returns the response in JSON format
# response.json()['iss_position] - returns a specific object from the response

data = response.json()

longitude = data["iss_position"]["longitude"]
latitude = data["iss_position"]["latitude"]

iss_position = (longitude, latitude)

print(iss_position)