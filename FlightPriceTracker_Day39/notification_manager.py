import smtplib
import config
from data_manager import DataManager


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.message = None

    def send_mail(self, message):
        self.message = message
        data_manager = DataManager()
        users = data_manager.get_users()
        for user in users:
            with smtplib.SMTP('smtp.gmail.com', 587) as connection:
                connection.starttls()
                connection.login(config.sender_email, config.sender_password)
                connection.sendmail(from_addr=config.sender_email, to_addrs=user['email'], msg=self.message)
