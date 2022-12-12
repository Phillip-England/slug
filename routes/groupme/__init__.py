import os

from ._login import login
from ._send_message import send_message

class groupme:

    def __init__(self):
        
        self.testing_account = {
            'username': os.environ.get("GROUPME_TESTING_USERNAME"),
            'password': os.environ.get("GROUPME_TESTING_PASSWORD"),
            'chat_aria_label': 'Chat testing',
            'message_input_id': 'message-composer-90967387',
        }

        self.southroads_account = {
            'username': os.environ.get("GROUPME_USERNAME"),
            'password': os.environ.get("GROUPME_PASSWORD"),
            'chat_aria_lable': 'Chat Southroads Leadership',
            'message_input_id': 'message-composer-15570590',
        }

    def login(self, driver, config, account): login(driver, config, account)
    def send_message(self, driver, config, account, message): send_message(driver, config, account, message)