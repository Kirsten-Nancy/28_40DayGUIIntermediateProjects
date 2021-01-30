import datetime as dt
import random
import smtplib

sender_email = "sender@gmail.com"
password = "password"

now = dt.datetime.now()
today = now.weekday()

with open("quotes.txt") as file:
    quotes_list = file.readlines()
    today_quote = random.choice(quotes_list)

if today == 0:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=sender_email, password=password)
        connection.sendmail(from_addr=sender_email,
                            to_addrs="receiver@yahoo.com",
                            msg=f"Subject:Quote of the day \n\n{today_quote}")