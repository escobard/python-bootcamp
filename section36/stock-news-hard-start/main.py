import requests

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"


## STEP 1: Use https://www.alphavantage.co/
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
#HINT 1: Get the closing price for yesterday and the day before yesterday. Find the positive difference between the two prices. e.g. 40 - 20 = -20, but the positive difference is 20.
#HINT 2: Work out the value of 5% of yerstday's closing stock price.

parameters = {
  "function": 'TIME_SERIES_DAILY',
  "symbol": "MSFT",
  "apikey": 'demo'
}

stock_response = requests.get(url=STOCK_ENDPOINT, params=parameters)

stock_response.raise_for_status()
stock_data = stock_response.json()["Time Series (Daily)"]
stock_data_yesterday_key = list(stock_response.json()["Time Series (Daily)"].keys())[0]
stock_data_day_before_yesterday_key = list(stock_response.json()["Time Series (Daily)"].keys())[1]
stock_price_yesterday = float(stock_data[stock_data_yesterday_key]["4. close"])
stock_price_day_before_yesterday = float(stock_data[stock_data_day_before_yesterday_key]["4. close"])
stock_price_percentage_change = (stock_price_day_before_yesterday / stock_price_yesterday) * 100
print(stock_price_percentage_change)

## STEP 2: Use https://newsapi.org/docs/endpoints/everything
# Instead of printing ("Get News"), actually fetch the first 3 articles for the COMPANY_NAME. 
#HINT 1: Think about using the Python Slice Operator



## STEP 3: Use twilio.com/docs/sms/quickstart/python
# Send a separate message with each article's title and description to your phone number. 
#HINT 1: Consider using a List Comprehension.



#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

