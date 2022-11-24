import pyautogui
import os

class config:
    def __init__(self):

        #global settings
        self.max_wait_time = 20
        self.pyautogui_type_speed = 0.1
        # determines how many times we will run an operation before exiting
        self.max_loop = 5

        #cfa login settings
        self.cfa_home_url = 'https://www.cfahome.com'
        self.cfa_username_input_id = 'okta-signin-username'
        self.cfa_password_input_id = 'input59'
        self.cfa_reports_and_tools_dropdown_id = 'navbarDropdown-Reports_and_Tools' #used to check if cfahome.com is fully loaded

        #service point main page settings
        self.service_point_url = 'https://rsmw.cfahome.com/SMW18-00/StoreMgmtKOSignin.aspx?Store=03253'
        self.service_point_login_input_id = 'MainContent_txtEchoWindow'
        self.service_point_submit_id = 'MainContent_btnEnter'
        self.service_point_make_favorite_button_id = 'btnMakeFavorite' #used to check is page is fully loaded

        #daypart activity report settings
        self.daypart_activity_url = 'https://rsmw.cfahome.com/SMW18-00/StoreMgmtKOReportDayPart.aspx'
        self.daypart_activity_wage_input_color = (255, 255, 255)
        self.daypart_activity_wage_input_cords = (538, 419)
        self.daypart_activity_start_date_id = 'MainContent_BusDate1_B-1Img'
        self.daypart_activity_end_date_id = 'MainContent_BusDate2_B-1Img'
        self.daypart_activity_submit_id = 'MainContent_btnGenerateButton'
        self.daypart_activity_bad_day_id = 'InformationalPopup_HCB-1'
        self.daypart_activity_default_download_path = os.path.join(os.environ.get('HOME'), 'Downloads', 'Daypart Activity Report.pdf')

        # sales activity report settings
        self.sales_activity_url = 'https://rsmw.cfahome.com/SMW18-00/CFASalesActivityReport.aspx'
        self.sales_activity_date_input_id = 'MainContent_cfaCommonReportInputInterface1_startBusinessDateWithTime_I'
        self.sales_activity_bad_day_id = 'InformationalPopup_HCB-1'
        self.sales_activity_submit_id = 'MainContent_cfaCommonReportInputInterface1_btnGenerateButton'
        self.sales_activity_default_download_path = os.path.join(os.environ.get('HOME'), 'Downloads', 'Sales Activity Report.pdf')


        # sales tracking google form settings
        self.sales_tracking_form_url = 'https://forms.gle/GuYmkRqdfRpgKSYB6'
        self.sales_form_purple_header_cords = (441, 139)
        self.sales_form_purple_color = (103, 58, 183)
        self.first_sales_input_cords = (429, 365)

        #cem page settings
        self.cem_url = 'https://www.cfahome.com/go/appurl.go?app=SMGCLM'
        self.cem_report_builder_url = 'https://reporting.smg.com/ReportBuilder.aspx'
        self.cem_report_type_dropdown_cords = (325, 371)
        self.cem_blue_banner_cords = (120, 256)
        self.cem_blue_banner_color = (9, 118, 214)
        self.cem_date_range_dropdown_cords = (294, 511)
        self.cem_options = (986, 410)
        self.report_builder_button_id = 'rbBuildReportBTN'
        self.cem_score_selection_id = 'rbSurveyItemSEL1_chosen'
        self.cem_date_range_id = 'rbDateRangeSEL'
        self.cem_download_menu_button = 'rvSaveReportBTN'
        self.download_cem_data_button = (1123, 303)
        self.cem_pdf_option = (347, 599)
        self.cem_portrait_pdf_id = 'rvsPDFLBL'
        self.cem_download_button_id = 'rvsDownloadBTN'
        self.cem_report_download_path = os.path.join(os.environ.get('HOME'), 'Downloads', 'FullScale_Report.PDF')


