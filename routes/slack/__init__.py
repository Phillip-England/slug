import os

from ._login import login
from ._schedule_message import schedule_message
from ._send_message import send_message

class slack:
    def __init__(self):

        self.testing_account = {
            'login_url': os.environ.get("SLACK_TESTING_LOGIN_PAGE"),
            'home_url': os.environ.get("SLACK_TESTING"),
            'email': os.environ.get("SLACK_EMAIL"),
            'password': os.environ.get("SLACK_PASSWORD")
        },

        self.southroads_account = {
            'login_url': os.environ.get("SLACK_LOGIN_PAGE"),
            'home_url': os.environ.get("SLACK_CFASOUTHROADS"),
            'email': os.environ.get("SLACK_EMAIL"),
            'password': os.environ.get("SLACK_PASSWORD")
        }

    def login(self, driver, config, account): login(driver, config, account)
    def schedule_message(self, driver, config, account, message): schedule_message(driver, config, account, message)
    def send_message(self, driver, config, account, message): send_message(driver, config, account, message)
    