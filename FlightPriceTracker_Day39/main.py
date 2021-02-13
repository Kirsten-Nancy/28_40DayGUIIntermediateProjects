from notification_manager import  NotificationManager
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData

data_manager = DataManager()
sheet_data = data_manager.get_destination_cities()
notification_manager = NotificationManager()
for i in range(len(sheet_data)):
    flight_search = FlightSearch(sheet_data[i]['city'])
    flight = flight_search.search_flights(sheet_data[i]['iataCode'])
    if flight is None:
        continue
    elif flight.price < sheet_data[i]['lowestPrice']:
        print(f'Found a cheaper flight to {flight.arr_city_name}')
        message = f'Subject: Flight updates \n\nFound a cheap flight to ' \
                  f'one of your destinations. Fly from {flight.dept_city_name}-{flight.dept_airport_iata_code}' \
                  f' to {flight.arr_city_name}-{flight.arr_airport_iata_code} for only ${flight.price} from' \
                  f' {flight.outbound_date} to {flight.inbound_date}. '
        if flight.stop_overs > 0:
            message += f'Flight has {flight.stop_overs}, via {flight.via_city}.'
        message += f'\nhttps://www.google.co.uk/flights?hl=en#flt={flight.dept_airport_iata_code}.{flight.arr_airport_iata_code}.{flight.outbound_date}*{flight.dept_airport_iata_code}.{flight.arr_airport_iata_code}.{flight.inbound_date}'
        notification_manager.send_mail(message=message)

# flight_data = FlightData(sheet_data)
# for i in range(len(sheet_data)):
#     if sheet_data[i]['iataCode'] == '':
#         flight_search = FlightSearch(sheet_data[i]['city'])
#         sheet_data[i]['iataCode'] = flight_search.get_iata_code()
# row_data = {
#     'price': {
#         'iataCode': sheet_data[i]['iataCode']
#     }
# }
# data_manager.put_request(i+2, row_data)
# print(sheet_data)
