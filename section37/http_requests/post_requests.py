# for this projet we will be using pixela to track habits
## pixella website - https://pixe.la/
### navigating to "how to use" shows quick start instructions
import requests
USERNAME = 'escobard'
TOKEN = 'random_token'

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
  'id': 'python-code',
  'name': 'python-code',
  'unit': 'hours',
  'type': 'int',
  'color': 'sora'
}

request_headers: dict[str, str] = {
  'X-USER-TOKEN': TOKEN
}

response = requests.post(url=graph_endpoint, headers=request_headers, json=graph_parameters)
print(response.text)
# graph can be seen at https://pixe.la/v1/users/escobard/graphs/python-code