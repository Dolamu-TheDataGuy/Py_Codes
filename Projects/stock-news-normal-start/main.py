import requests
from collections.abc import Mapping
import json
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_API_KEY = "OVPY5SF17FCAQ7HB"
NEWS_API_KEY = "6f3a05e1fc604e67af40b5760c21dd18"
TWILIO_SID = "AC0a6d75bed8596fe6d6c87d8406f622b1"
TWILIO_AUTH_TOKEN = "c3937784efa39fa3d98147a15e0317d2"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

stock_params = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY,
}

response = requests.get(url=STOCK_ENDPOINT, params=stock_params)
# print(response.json())

# gets data and put it in a json file
data = response.json()  # python object
with open("data.json", "w") as f:
    json.dump(data, f, indent=4)  # convert a python object to json, without s

# get yesterday's closing price
data = data["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]  # outputs a list of dictionaries
# print(data_list)
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]
print(yesterday_closing_price)

# get the day before yesterday's price.
day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]
print(day_before_yesterday_closing_price)

# TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20.
#  Hint: https://www.w3schools.com/python/ref_func_abs.asp
# find difference between prices to know if there was inc or decrease.
difference = (float(yesterday_closing_price) - float(day_before_yesterday_closing_price))
print(difference)
up_down = None
if difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"

# TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day
#  before yesterday.
# find percentage difference between closing price yesterday and closing price the day before.
diff_percent = round(((float(yesterday_closing_price) / float(day_before_yesterday_closing_price)) - 1) * 100)
print(diff_percent)

# TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").
## STEP 2: https://newsapi.org/

# TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.
if abs(diff_percent) > 5:
    news_params = {
        "apiKey": NEWS_API_KEY,
        "qInTitle": COMPANY_NAME,
    }
    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    articles = news_response.json()['articles']
    # Use slice operator to get first 3 content of the article list.
    three_articles = articles[:3]

    formatted_articles = [
        f"{STOCK_NAME}: {up_down}{diff_percent}%\nHeadline: {articles['title']}. \nBrief: {articles['description']}" for
        articles in three_articles]

    # TODO 9. - Send each article as a separate message via Twilio.
    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
    for article in formatted_articles:
        message = client.messages.create(
            body=article,
            from_="+17605238493",
            to='+2348165539137'
        )

    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    # to send a separate message with each article's title and description to your phone number.

#


# Optional TODO: Format the message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
