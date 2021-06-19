import requests
import datetime
import os
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_KEY = os.environ.get('STOCK_KEY')
NEWS_KEY = os.environ.get('NEWS_KEY')

parameters = {"function": "TIME_SERIES_DAILY",
              "symbol": STOCK,
              "apikey": STOCK_KEY}

response_stock = requests.get("https://www.alphavantage.co/query", params=parameters)
response_stock.raise_for_status()

# print(response_stock.json())

data = response_stock.json()["Time Series (Daily)"]

data_list = [value for (key,value) in data.items()]

yesterday_stock_price = float(data_list[0]["4. close"])
day_before_stock_price = float(data_list[1]["4. close"])

difference = (yesterday_stock_price - day_before_stock_price)/day_before_stock_price*100

get_news = False

stock_change = ""

if difference >=5:

    if yesterday_stock_price >= day_before_stock_price:
        print("get news")
        get_news = True
        stock_change = f"🔺{round(difference)}"
    else:
        print("get news")
        get_news = True
        stock_change = f"🔻{round(difference)}"


    parameters_news = {"apiKey": NEWS_KEY,
                       "q": COMPANY_NAME}

    response_news = requests.get("https://newsapi.org/v2/everything", params=parameters_news)
    response_news.raise_for_status()

    news = []
    news.append(response_news.json()["articles"][0])
    news.append(response_news.json()["articles"][1])
    news.append(response_news.json()["articles"][2])


    account_sid = os.environ.get(['TWILIO_ACCOUNT_SID'])
    auth_token = os.environ.get(['TWILIO_AUTH_TOKEN'])

    client = Client(account_sid, auth_token)

    for new in news:
        line = STOCK
        line += stock_change
        line += "\nHeadline: "
        line += new["title"]
        line += "\nBrief: "
        line += new["description"]
        message = client.messages \
                        .create(
                             body=line,
                             from_=os.environ.get('TWILIO_NUMBER'),
                             to=os.environ.get('VERIFIED_NUMBER')
                         )

        print(message.sid)