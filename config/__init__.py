import pyautogui
import os

class config:
    def __init__(self):

        #global settings
        self.max_wait_time = 60 
        self.pyautogui_type_speed = 0.05
        self.slack_scheduled_message_time = '8:00 AM'
        self.testing_slack = True
        self.clear_downloads = True
        self.testing_groupme = True

        # paths
        self.cem_report_download_path_current_month = os.path.join(os.environ.get('HOME'), 'Downloads', 'FullScale_Report.PDF')
        self.cem_report_download_path_ninty_day_rolling = os.path.join(os.environ.get('HOME'), 'Downloads', 'FullScale_Report (1).PDF')
        self.cem_report_download_path_year_to_date = os.path.join(os.environ.get('HOME'), 'Downloads', 'FullScale_Report (2).PDF')
        self.daypart_activity_default_download_path = os.path.join(os.environ.get('HOME'), 'Downloads', 'Daypart Activity Report.pdf')
        self.sales_activity_default_download_path = os.path.join(os.environ.get('HOME'), 'Downloads', 'Sales Activity Report.pdf')
        self.deferred_order_default_download_path = os.path.join(os.environ.get("HOME"), 'Downloads', 'Deferred Orders Reports.pdf')

        # slack



        #envysion
        self.envysion_email_input_id = 'login-username'
        self.envysion_password_input_id = 'login-password'
        self.envysion_loading_element_class_name = 'jss92'

        # textfree
        self.text_free_username_id = 'username'
        self.text_free_password_id = 'password'
        self.text_free_close_google_contact_id = 'SyncContactsXDismissPopup'
        self.text_free_logo_id = 'logo'
        self.text_free_compose_id = 'startNewConversationButton'
        self.text_free_contact_input_id = 'contactInput'
        self.text_free_message_input_class_name = 'messageFormContainer'
        self.text_free_send_button = 'sendButton'

        # groupme

        self.groupme_chats_class_name = 'list-item'
        self.groupme_testing_aria_label = 'Chat testing'
        self.groupme_southroads_leadership_aria_label = 'Chat Southroads Leadership'
        self.groupme_testing_messaging_area_id = 'message-composer-90967387'
        self.groupme_southroads_leadership_messaging_area_id = 'message-composer-15570590'


