import requests
import datetime as dt
import smtplib

SENDER_EMAIL = 'sender@gmail.com'
PASSWORD = 'password'

LONGITUDE = 126.676743
LATITUDE = 45.774460
LOCAL_UTC_OFFSET = 8

def utc_to_local(utc_hour):
    utc_hour += LOCAL_UTC_OFFSET
    if LOCAL_UTC_OFFSET > 0:
        if utc_hour > 23:
            utc_hour -= 24
    elif LOCAL_UTC_OFFSET < 0:
        if utc_hour < 0:
            utc_hour += 24
    return utc_hour

def iss_proximity():
    iss_response = requests.get(url='http://api.open-notify.org/iss-now.json')
    iss_response.raise_for_status()

    iss_data = iss_response.json()
    longitude = float(iss_data['iss_position']['longitude'])
    latitude = float(iss_data['iss_position']['latitude'])
    long_difference = longitude - LONGITUDE
    lat_difference = latitude - LATITUDE
    print(long_difference)
    print(lat_difference)
    if 5 >= long_difference >= -5 and 5 >= lat_difference >= -5:
        return True
    return False

def night_time():
    parameters = {
        'lng': LONGITUDE,
        'lat': LATITUDE,
        'formatted': 0
    }
    response = requests.get(url='https://api.sunrise-sunset.org/json', params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data['results']['sunrise'].split('T')[1].split(':')[0])
    sunset = int(data['results']['sunset'].split('T')[1].split(':')[0])

    local_sunrise = utc_to_local(sunrise)
    local_sunset = utc_to_local(sunset)
    print(local_sunrise)
    print(local_sunset)

    current_hour = dt.datetime.now().hour
    if local_sunset <= current_hour <= local_sunrise:
        return True
    return False


if iss_proximity() and night_time():
    with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
        connection.starttls()
        connection.login(user=SENDER_EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=SENDER_EMAIL, to_addrs='receiver@gmail.com',
                            msg="Subject:ISS Notifier\n\nThe ISS is in your vicinity, look up!")
else:
    print("It's long gone")
