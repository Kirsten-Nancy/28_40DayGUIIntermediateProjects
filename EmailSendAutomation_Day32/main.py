import pandas
import random
import smtplib
import datetime as dt
import config

now = dt.datetime.now()
day = now.day
month = now.month

birthdays = pandas.read_csv("birthdays.csv")
for index, row in birthdays.iterrows():
    if day == row['day'] and month == row['month']:
        name = row['name']
        email = row['email']

        number = random.randint(1, 3)
        with open(f'letter_templates/letter_{number}.txt') as file:
            data = file.read()
            bday_wish = data.replace('[NAME]', name)
            # print(bday_wish)

        sender_email = config.sender_email
        password = config.sender_password

        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=sender_email, password=password)
            connection.sendmail(from_addr=sender_email, to_addrs=email,
                                msg=f"Subject:Happy Birthday Wishes\n\n{bday_wish}")





