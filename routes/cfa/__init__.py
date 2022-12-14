import os

from ._login_home import login_home
from ._login_service_point import login_service_point
from ._daypart_activity import daypart_activity
from ._sales_activity import sales_activity
from ._cem_report_builder import cem_report_builder
from ._catering_orders import catering_orders
from ._hr_payroll import hr_payroll

class cfa:

    def __init__(self):
        
        # login settings
        self.cfahome_url = os.environ.get("CFA_HOME_URL")
        self.login_username_id = 'okta-signin-username'
        self.login_password_id = 'input59'
        self.homepage_reports_id = 'navbarDropdown-Reports_and_Tools'

        # service point settings
        self.service_point_url = os.environ.get("SERVICE_POINT_URL")
        self.service_point_login_input_id = 'MainContent_txtEchoWindow'
        self.service_point_submit_id = 'MainContent_btnEnter'
        self.service_point_favorite_button_id = 'btnMakeFavorite'

        # daypart activity settings
        self.daypart_activity_url = os.environ.get("DAYPART_ACTIVITY_URL")
        self.daypart_activity_start_date_id = 'MainContent_BusDate1_B-1Img'
        self.daypart_activity_end_date_id = 'MainContent_BusDate2_B-1Img'
        self.daypart_activity_submit_id = 'MainContent_btnGenerateButton'
        self.daypart_activity_bad_day_id = 'InformationalPopup_HCB-1'

        # sales activity settings
        self.sales_activity_url = os.environ.get("SALES_ACTIVITY_URL")
        self.sales_activity_date_input_id = 'MainContent_cfaCommonReportInputInterface1_startBusinessDateWithTime_I'
        self.sales_activity_bad_day_id = 'InformationalPopup_HCB-1'
        self.sales_activity_submit_id = 'MainContent_cfaCommonReportInputInterface1_btnGenerateButton'

        # cem settings
        self.cem_url_true = os.environ.get("CEM_TRUE_URL")
        self.cem_main_logo_id = 'clientLogo'
        self.cem_report_builder_url = os.environ.get("REPORT_BUILDER_URL")
        self.cem_report_builder_button_id = 'rbBuildReportBTN'
        self.cem_report_type_dropdown_id = 'rbReportTypeSEL'
        self.cem_report_date_range_dropdown_id = 'rbDateRangeSEL'
        self.cem_report_builder_start_date_id = 'rbStartDateTB'
        self.cem_report_builder_end_date_id = 'rbEndDateTB'
        self.cem_report_builder_cem_selection_class_name = 'default'
        self.cem_report_builder_build_button_id = 'rbBuildReportBTN'
        self.cem_report_builder_scores_loaded_id = 'rvTitleSpan1'
        self.cem_download_menu_button = 'rvSaveReportBTN'
        self.cem_download_menu_id = 'rvsTitleDiv'
        self.cem_portrait_pdf_id = 'rvsPDFLBL'
        self.cem_download_button_id = 'rvsDownloadBTN'

        # catering settings
        self.catering_order_url = os.environ.get('DEFERRED_ORDER_REPORT')
        self.catering_start_date_id = 'MainContent_BusDate1_I'
        self.catering_end_date_id = 'MainContent_BusDate2_I'
        self.catering_submit_id = 'MainContent_btnGenerateButton'

        # hy payroll settings
        self.hr_all_reports_id = 'allreports'
        self.hr_bday_report_id = 'employeebirthdate'
        self.hr_bday_loading_element_id = 'dempTable-0-0'

    # routes
    def login_home(self, driver, config): login_home(self, driver, config)
    def login_service_point(self, driver, config): login_service_point(self, driver, config)
    def daypart_activity(self, driver, config, date): daypart_activity(self, driver, config, date)
    def sales_activity(self, driver, config, date): sales_activity(self, driver, config, date)
    def cem_report_builder(self, driver, config): cem_report_builder(self, driver, config)
    def catering_orders(self, driver, config, date): catering_orders(self, driver, config, date)
    def hr_payroll(self, driver, config, date): hr_payroll(self, driver, config, date)