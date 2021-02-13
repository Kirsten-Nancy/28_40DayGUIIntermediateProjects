import requests
import config

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
       pass

    def get_destination_cities(self):
        response = requests.get(config.SHEETY_FLIGHTS_ENDPOINT)
        return response.json()['prices']

    def get_users(self):
        response = requests.get(config.SHEETY_USERS_ENDPOINT)
        return response.json()['users']

    # def update_dest_cities(self, row_id, body):
    #     response = requests.put(url=f"{config.SHEETY_FLIGHTS_ENDPOINT}/{row_id}",
    #                                      headers={"content-type": "application/json"}, json=body)
    #
    #     print(response.text)