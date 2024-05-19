# for this projet we will be using pixela to track habits
## pixella website - https://pixe.la/
### navigating to "how to use" shows quick start instructions
import requests
from datetime import datetime

USERNAME = 'escobard'
TOKEN = 'random_token'
GRAPH_NAME= 'python-code'

pixela_endpoint: str = 'https://pixe.la/v1/users'

# step 1. call users API to create user
## https://docs.pixe.la/entry/post-user
user_parameters: dict[str, str] = {
  'token': TOKEN,
  'username': USERNAME,
  'agreeTermsOfService': 'yes',
  'notMinor': 'yes'
}
# response = requests.post(url=pixela_endpoint, json=user_parameters)
# print(response)

# step 2. create a graph definition
## https://docs.pixe.la/entry/post-graph
graph_endpoint: str = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_parameters: dict[str, str] = {
  'id': GRAPH_NAME,
  'name': GRAPH_NAME,
  'unit': 'hours',
  'type': 'int',
  'color': 'sora'
}

request_headers: dict[str, str] = {
  'X-USER-TOKEN': TOKEN
}

# response = requests.post(url=graph_endpoint, headers=request_headers, json=graph_parameters)
# print(response.text)
# graph can be seen at https://pixe.la/v1/users/escobard/graphs/python-code.html

# step 3. post a pixel to the graph
## https://docs.pixe.la/entry/post-pixel

graph_update_endpoint: str = f"https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPH_NAME}"

# can format python date times in several different ways
## https://www.w3schools.com/python/python_datetime.asp
today = datetime.now()
formatted_date_time = today.strftime("%Y%m%d")

graph_update_parameters: dict[str, str] = {
  'date': formatted_date_time,
  'quantity': '3'
}

# response = requests.post(url=graph_update_endpoint, headers=request_headers, json=graph_update_parameters)
# print(response.text)

# step 4. put pixel
## https://docs.pixe.la/entry/put-graph
graph_put_endpoint: str = f"{graph_update_endpoint}/{formatted_date_time}"
graph_put_parameters = {
  'quantity': '3'
}

# response = requests.put(url=graph_put_endpoint, headers=request_headers, json=graph_put_parameters)
# print(response.text)

# step 5. delete pixel
## https://docs.pixe.la/entry/delete-pixel
# response = requests.delete(url=graph_put_endpoint, headers=request_headers)
# print(response.text)