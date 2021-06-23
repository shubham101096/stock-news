# stock-news-python
This python program helps the user in getting alerts related to stock prices of the company he is interested in.
This code can be run daily on the cloud (e.g on python anywhere). 
It checks if the stock price of a company( can be set by the user) changed by more than 5% over the last two days. If it is true then 3 SMS containing latest 3 news related to that company are sent to his mobile number. These SMS also mention the change in stock price.
The stock price changes are fetched using alpha vantage Stock API.
Below is the screenshot of one of the SMS sent when Tesla stock price fell 6%.

![alt text](https://github.com/shubham101096/stock-news-python/blob/master/screenshots/news_alert.jpeg)
