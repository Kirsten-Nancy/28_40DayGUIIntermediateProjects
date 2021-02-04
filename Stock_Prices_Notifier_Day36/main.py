import requests
from twilio.rest import Client
import config

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

ALPHA_API_KEY = config.ALPHAVANTAGE_API_KEY
NEWS_API_KEY = config.NEWS_API_KEY

account_sid = config.account_sid
auth_token = config.auth_token

alpha_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": ALPHA_API_KEY
}
alpha_response = requests.get("https://www.alphavantage.co/query", params=alpha_parameters)
alpha_response.raise_for_status()
data_dict = alpha_response.json()["Time Series (Daily)"]
recent = list(data_dict)[:2]
yesterday_closing_price = float(data_dict[recent[0]]['4. close'])
previous_day_closing_price = float(data_dict[recent[1]]['4. close'])

difference = yesterday_closing_price-previous_day_closing_price
if difference > 0:
    emoji = "🔺"
else:
    emoji = "🔻"

percentage_diff = round((difference/yesterday_closing_price) * 100)

if abs(percentage_diff) > 5:
    news_parameters = {
           "qInTitle": COMPANY_NAME,
           "sortBy": "popularity",
           "apiKey": NEWS_API_KEY
    }
    news_response = requests.get("http://newsapi.org/v2/everything", params=news_parameters)
    news_articles = news_response.json()['articles'][:3]

    client = Client(account_sid, auth_token)
    for news in news_articles:
        body = f"{STOCK_NAME}: {emoji}{percentage_diff}% \n\n Headline: {news['title']} \n\n Brief: {news['description']}"
        message = client.messages \
            .create(
            body=body,
            from_=config.twilio_number,
            to=config.personal_number
        )

        print(message.sid)


