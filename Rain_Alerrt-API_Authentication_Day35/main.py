import requests

API_KEY = "API_KEY"
parameters = {
    "lat": 45.774460,
    "lon": 126.676743,
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
    print(weather_data_id)
    if weather_data_id < 700:
        print("Bring an umbrella")
        break
