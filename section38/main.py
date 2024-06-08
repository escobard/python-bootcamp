## build a workout tracker project
## inspired by openai api - https://openai.com/index/openai-api/

## Step 1 - copy google worksheet, sign up to nutritionux (https://www.nutritionix.com/business/api) and build env variable constants for APP_ID and API_KEY

import os

APP_ID: str = os.environ.get('APP_ID')
API_KEY: str = os.environ.get('API_KEY')

print(APP_ID, API_KEY)
