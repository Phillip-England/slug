import pyautogui
import os

class config:
    def __init__(self):

        #global settings
        self.max_wait_time = 60 
        self.pyautogui_type_speed = 0.05
        self.slack_scheduled_message_time = '8:00 AM'
        self.testing_slack = False
        self.clear_downloads = True
        self.testing_groupme = False

        # paths
        self.cem_report_download_path_current_month = os.path.join(os.environ.get('HOME'), 'Downloads', 'FullScale_Report.PDF')
        self.cem_report_download_path_ninty_day_rolling = os.path.join(os.environ.get('HOME'), 'Downloads', 'FullScale_Report (1).PDF')
        self.cem_report_download_path_year_to_date = os.path.join(os.environ.get('HOME'), 'Downloads', 'FullScale_Report (2).PDF')
        self.daypart_activity_default_download_path = os.path.join(os.environ.get('HOME'), 'Downloads', 'Daypart Activity Report.pdf')
        self.sales_activity_default_download_path = os.path.join(os.environ.get('HOME'), 'Downloads', 'Sales Activity Report.pdf')
        self.deferred_order_default_download_path = os.path.join(os.environ.get("HOME"), 'Downloads', 'Deferred Orders Reports.pdf')