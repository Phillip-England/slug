import pyautogui
import os

class config:
    def __init__(self):

        #global settings
        self.max_wait_time = 20 # how long will we wait for a page to load
        self.pyautogui_type_speed = 0.05
        # determines how many times we will run an operation before exiting
        self.max_loop = 5
        self.refresh_wait_time = 20 # how long to wait before refreshing
        self.slack_scheduled_message_time = '8:00 AM'
        self.testing_slack = True
        self.clear_downloads = True


        #cfa login settings
        self.cfa_home_url = os.environ.get("CFA_HOME_URL")
        self.cfa_username_input_id = 'okta-signin-username'
        self.cfa_password_input_id = 'input59'
        self.cfa_reports_and_tools_dropdown_id = 'navbarDropdown-Reports_and_Tools' #used to check if cfahome.com is fully loaded

        #service point main page settings
        self.service_point_url = os.environ.get("SERVICE_POINT_URL")
        self.service_point_login_input_id = 'MainContent_txtEchoWindow'
        self.service_point_submit_id = 'MainContent_btnEnter'
        self.service_point_make_favorite_button_id = 'btnMakeFavorite' #used to check is page is fully loaded

        #daypart activity report settings
        self.daypart_activity_url = os.environ.get("DAYPART_ACTIVITY_URL")
        self.daypart_activity_start_date_id = 'MainContent_BusDate1_B-1Img'
        self.daypart_activity_end_date_id = 'MainContent_BusDate2_B-1Img'
        self.daypart_activity_submit_id = 'MainContent_btnGenerateButton'
        self.daypart_activity_bad_day_id = 'InformationalPopup_HCB-1'
        self.daypart_activity_default_download_path = os.path.join(os.environ.get('HOME'), 'Downloads', 'Daypart Activity Report.pdf')

        # sales activity report settings
        self.sales_activity_url = os.environ.get("SALES_ACTIVITY_URL")
        self.sales_activity_date_input_id = 'MainContent_cfaCommonReportInputInterface1_startBusinessDateWithTime_I'
        self.sales_activity_bad_day_id = 'InformationalPopup_HCB-1'
        self.sales_activity_submit_id = 'MainContent_cfaCommonReportInputInterface1_btnGenerateButton'
        self.sales_activity_default_download_path = os.path.join(os.environ.get('HOME'), 'Downloads', 'Sales Activity Report.pdf')

        # sales tracking google form settings
        self.sales_tracking_form_url = os.environ.get("SALES_GOOGLE_FORM")
        self.sales_form_input_class_name = 'whsOnd'
        self.sales_form_submit_class_name = 'NPEfkd'

        #cem page settings
        self.cem_url_true = os.environ.get("CEM_TRUE_URL")
        self.cem_url_redirect = os.environ.get("CEM_REDIRECT_URL")
        self.cem_loaded_id = 'clientLogo'
        self.cem_report_builder_url = os.environ.get("REPORT_BUILDER_URL")
        self.report_builder_button_id = 'rbBuildReportBTN'
        self.report_type_dropdown_id = 'rbReportTypeSEL'
        self.report_date_range_dropdown_id = 'rbDateRangeSEL'
        self.report_builder_start_date_id = 'rbStartDateTB'
        self.report_builder_end_date_id = 'rbEndDateTB'
        self.report_builder_cem_selection_class_name = 'default'
        self.report_builder_build_button_id = 'rbBuildReportBTN'
        self.report_builder_scores_loaded_id = 'rvTitleSpan1'
        self.cem_download_menu_button = 'rvSaveReportBTN'
        self.cem_download_menu_id = 'rvsTitleDiv'
        self.cem_portrait_pdf_id = 'rvsPDFLBL'
        self.cem_download_button_id = 'rvsDownloadBTN'
        self.cem_report_download_path_current_month = os.path.join(os.environ.get('HOME'), 'Downloads', 'FullScale_Report.PDF')
        self.cem_report_download_path_ninty_day_rolling = os.path.join(os.environ.get('HOME'), 'Downloads', 'FullScale_Report (1).PDF')
        self.cem_report_download_path_year_to_date = os.path.join(os.environ.get('HOME'), 'Downloads', 'FullScale_Report (2).PDF')


        # cem google form
        self.cem_tracking_form_url = os.environ.get("CEM_GOOGLE_FORM_URL")
        self.cem_tracking_loading_element = 'whsOnd'
        self.cem_tracking_inputs_class_name = 'whsOnd'
        self.cem_tracking_submit_button = 'NPEfkd'

        # cem spreadsheet
        self.cem_spreadsheet_url = os.environ.get("CEM_SPREADSHEET_URL")
        self.cem_spreadsheet_loading_element_class_name = 'gb_2'
        self.cem_spreadsheet_download_path = os.path.join(os.environ.get('HOME'), 'Downloads', "Data Scraping - CEM Data.csv")

        # slack
        self.slack_email_input_id = 'email'
        self.slack_password_input_id = 'password'
        self.slack_sign_in_button_id = 'signin_btn'
        self.slack_loading_element_id = 'c-coachmark-anchor'
        self.slack_message_element_class_name = 'ql-editor'
        self.slack_schedule_button_class_name = 'c-button-unstyled'
        self.slack_schedule_button_aria_label = 'Schedule for later'
        self.slack_custom_time_button_class_name = 'c-menu_item__label'
        self.slack_time_slot_class_name = 'c-select_input__content_text'
        self.slack_schedule_message_button_class_name = 'c-button'


        #envysion
        self.envysion_email_input_id = 'login-username'
        self.envysion_password_input_id = 'login-password'
        self.envysion_loading_element_class_name = 'jss92'



