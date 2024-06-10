## build a workout tracker project
## inspired by openai api - https://openai.com/index/openai-api/

## Step 1 - copy google worksheet, sign up to nutritionux (https://www.nutritionix.com/business/api) and build env variable constants for APP_ID and API_KEY

import os
import requests
from datetime import datetime

## how to set env variables for debugging in pycharm: https://stackoverflow.com/questions/42708389/how-to-set-environment-variables-in-pycharm

APP_ID: str = os.environ.get('APP_ID')
API_KEY: str = os.environ.get('API_KEY')
SHEETY_API_KEY: str = os.environ.get('SHEETY_API_KEY')

nutritionix_endpoint: str = 'https://trackapi.nutritionix.com/v2/natural/exercise'

user_input_question: str = 'Tell me which exercises you did: '

## Step 2 - using the Nutritionix API guide (https://docx.syndigo.com/developers/docs/nutritionix-api-guide), figure out how to print the exercise stats for plain text input

user_input: str = input(user_input_question)

## make a request to the natural language for exercise API - https://docx.syndigo.com/developers/docs/natural-language-for-exercise

nutritionix_request_headers: dict[str, str] = {
  'Content-type': 'application/json',
  'x-app-id': APP_ID,
  'x-app-key': API_KEY
}

nutritionix_request_body: dict[str, str] = {
  "query": user_input
}

response = requests.post(url=nutritionix_endpoint, headers=nutritionix_request_headers, json=nutritionix_request_body)

## Step 3 - authorize sheety and setup workouts google sheet - https://sheety.co/
## Step 4 - use sheety to generate a new row of data into the google excel sheet

duration = response.json()['exercises'][0]['duration_min']
calories = response.json()['exercises'][0]['nf_calories']
exercise = response.json()['exercises'][0]['name']

today = datetime.now()
formatted_date_time = today.strftime("%m/%d/%y")
formatted_hours = today.strftime("%H:%M:%S")

sheety_endpoint: str = f'https://api.sheety.co/{SHEETY_API_KEY}/workoutTracking/workouts'

sheety_request_body: dict[str, dict[str, str]] = {
  'workout': {
    'date': formatted_date_time,
    'time': formatted_hours,
    'exercise': exercise.title(),
    'duration': duration,
    'calories': calories
  }
}

sheety_request = requests.post(url=sheety_endpoint, json=sheety_request_body)

print(sheety_request.text)