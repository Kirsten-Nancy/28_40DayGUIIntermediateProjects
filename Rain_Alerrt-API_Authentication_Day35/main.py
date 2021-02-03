import requests
import smtplib
import config

sender_email = config.sender_email
password = config.sender_password

API_KEY = config.OWM_API_KEY
parameters = {
    "lat": -6.175110,
    "lon": 106.865036,
    "exclude": "current,minutely,daily",
    "units": "metric",
    "appid": API_KEY
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall", params=parameters)
response.raise_for_status()
weather_data = response.json()
list_12_hours = response.json()["hourly"][:12]

weather_data_list_ids = [response.json()["hourly"][i]["weather"][0]["id"] for i in range(len(list_12_hours))]

for i in range(len(list_12_hours)):
    weather_data_id = weather_data["hourly"][i]["weather"][0]["id"]
    if weather_data_id < 700:
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=sender_email, password=password)
            connection.sendmail(from_addr=sender_email,
                                to_addrs=config.receiver_email,
                                msg=f"Subject:Quote of the day \n\nBring an umbrella, it will rain later today")
        break