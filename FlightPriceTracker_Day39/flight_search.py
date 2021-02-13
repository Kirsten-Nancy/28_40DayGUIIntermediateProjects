import requests
import datetime
from flight_data import FlightData
import pprint
import config

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self, city_name):
        self.city_name = city_name
        self.headers = {
            "apikey": config.KIWI_APIKEY,
        }

    def get_iata_code(self):
        query = {
            "term": self.city_name,
            "location_types": "airport",
            "limit": 10,
        }
        response = requests.get(url="https://tequila-api.kiwi.com/locations/query", headers=self.headers, params=query)
        iata_code = response.json()['locations'][0]['city']['code']
        return iata_code

    def search_flights(self, code):
        tomorrow = datetime.datetime.today() + datetime.timedelta(days=1)
        six_month = datetime.datetime.today() + datetime.timedelta(days=1) + datetime.timedelta(days=180)
        tomorrow_formatted = str(tomorrow.strftime("%d/%m/%Y")).split(" ")[0]
        six_month_formatted = str(six_month.strftime("%d/%m/%Y")).split(" ")[0]

        query = {
            "fly_from": 'LON',
            "fly_to": code,
            "date_from": tomorrow_formatted,
            "date_to": six_month_formatted,
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 30,
            "flight_type": "round",
            "selected_cabins": "M",
            "max_stopovers": 0,
            "curr": "GBP",
        }
        response = requests.get("https://tequila-api.kiwi.com/v2/search", params=query, headers=self.headers)
        try:
            data = response.json()['data'][0]
        except IndexError:
            print(f'No flights available to {code}')
            query["max_stopovers"] = 1
            response = requests.get("https://tequila-api.kiwi.com/v2/search", params=query, headers=self.headers)
            data = response.json()['data'][0]
            flight_data = FlightData(
                price=data['price'],
                dept_city_name=data["route"][0]['cityFrom'],
                dept_airport_iata_code=data["route"][0]['flyFrom'],
                arr_city_name=data["route"][2]['cityTo'],
                arr_airport_iata_code=data["route"][2]['flyTo'],
                outbound_date=data["route"][0]["local_departure"].split("T")[0],
                inbound_date=data["route"][2]["local_departure"].split("T")[0],
                via_city=data["route"][1]['cityFrom'],
                stop_overs=1
            )
            return flight_data
        else:
            flight_data = FlightData(
                price=data['price'],
                dept_city_name=data['cityFrom'],
                dept_airport_iata_code=data['flyFrom'],
                arr_city_name=data['cityTo'],
                arr_airport_iata_code=data['flyTo'],
                outbound_date=data["route"][0]["local_departure"].split("T")[0],
                inbound_date=data["route"][1]["local_departure"].split("T")[0]
            )
            print(f'City: {flight_data.arr_city_name}: {flight_data.price}')
            return flight_data