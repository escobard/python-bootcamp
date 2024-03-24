import os
import requests
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"

NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

TWILIO_SID = os.environ.get('TWILIO_SID')
TWILIO_AUTH_TOKEN = os.environ.get('TWILIO_AUTH_TOKEN')
TWILIO_VIRTUAL_NUMBER = os.environ.get('TWILIO_VIRTUAL_NUMBER')
MY_NUMBER = os.environ.get('MY_NUMBER')

## STEP 1: Use https://www.alphavantage.co/
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
#HINT 1: Get the closing price for yesterday and the day before yesterday. Find the positive difference between the two prices. e.g. 40 - 20 = -20, but the positive difference is 20.
#HINT 2: Work out the value of 5% of yerstday's closing stock price.

stock_parameters = {
  "function": 'TIME_SERIES_DAILY',
  "symbol": "MSFT",
  "apikey": 'demo'
}

stock_response = requests.get(url=STOCK_ENDPOINT, params=stock_parameters)

stock_response.raise_for_status()
stock_data = stock_response.json()["Time Series (Daily)"]

stock_data_yesterday_key = list(stock_response.json()["Time Series (Daily)"].keys())[0]
stock_data_day_before_yesterday_key = list(stock_response.json()["Time Series (Daily)"].keys())[1]

stock_price_yesterday = float(stock_data[stock_data_yesterday_key]["4. close"])
stock_price_day_before_yesterday = float(stock_data[stock_data_day_before_yesterday_key]["4. close"])

stock_price_percentage_change = (stock_price_day_before_yesterday / stock_price_yesterday) * 100
print(stock_price_percentage_change)

if stock_price_percentage_change >= 105:
  print("Get news")

## STEP 2: Use https://newsapi.org/docs/endpoints/everything
# Instead of printing ("Get News"), actually fetch the first 3 articles for the COMPANY_NAME. 
#HINT 1: Think about using the Python Slice Operator

news_parameters = {
  "q": "Microsoft",
  "from": stock_data_yesterday_key,
  "sortBy": "popularity",
  "apiKey": os.environ.get('NEWS_API_KEY')
}

news_response = requests.get(url=NEWS_ENDPOINT, params=news_parameters)
news_response.raise_for_status()
# https://www.w3schools.com/python/ref_func_slice.asp
## :3 is a shorthand for python's slice operator
news_data = news_response.json()['articles'][:3]


## STEP 3: Use twilio.com/docs/sms/quickstart/python
# Send a separate message with each article's title and description to your phone number. 
#HINT 1: Consider using a List Comprehension.
condensed_news_alert = [f"Stock:{news_parameters["q"]} \nStock change: {stock_price_percentage_change - 100}% \nHeadline: {article['title']}. \nBrief: {article['description']}" for article in news_data]
print(condensed_news_alert)

## send sms to twilio
client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
for article in condensed_news_alert:
  message = client.messages.create(
    body=article,
    from_=TWILIO_VIRTUAL_NUMBER,
    to=MY_NUMBER
)