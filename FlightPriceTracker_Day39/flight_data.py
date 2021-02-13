class FlightData:
    #This class is responsible for structuring the flight data
    def __init__(self, price, dept_city_name, dept_airport_iata_code, arr_city_name,
                 arr_airport_iata_code, outbound_date, inbound_date, stop_overs=0,via_city=""):
        self.price = price
        self.dept_city_name = dept_city_name
        self.dept_airport_iata_code = dept_airport_iata_code
        self.arr_city_name = arr_city_name
        self.arr_airport_iata_code = arr_airport_iata_code
        self.outbound_date = outbound_date
        self.inbound_date = inbound_date
        self.stop_overs = stop_overs
        self.via_city = via_city
