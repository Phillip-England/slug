import os

from ._login import login
from ._schedule_message import schedule_message
from ._send_message import send_message
from ._southroads_cem_script import southroads_cem_script
from ._southroads_catering_script import southroads_catering_script

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

        # login settings
        self.login_email_id = 'email'
        self.login_password_id = 'password'
        self.login_submit_id = 'signin_btn'

        # chat settings
        self.loading_element_id = 'c-coachmark-anchor'
        self.message_element_class_name = 'ql-editor'
        self.schedule_button_class_name = 'c-button-unstyled'
        self.schedule_button_aria_label = 'Schedule for later'
        self.custom_time_button_class_name = 'c-menu_item__label'
        self.time_slot_class_name = 'c-select_input__content_text'
        self.schedule_message_button_class_name = 'c-button'

    # routes
    def login(self, driver, config, account): login(self, driver, config, account)
    def schedule_message(self, driver, config, account, message): schedule_message(self, driver, config, account, message)
    def send_message(self, driver, config, account, message): send_message(self, driver, config, account, message)
    
    # scripts
    def southroads_cem_script(self, engine): southroads_cem_script(engine)
    def southroads_catering_script(self, engine): southroads_catering_script(engine)