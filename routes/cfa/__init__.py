
from ._login_home import login_home
from ._login_service_point import login_service_point
from ._daypart_activity import daypart_activity
from ._sales_activity import sales_activity
from ._cem_report_builder import cem_report_builder
from ._catering_orders import catering_orders

class cfa:

    def __init__(self):
        pass

    def login_home(self, driver, config): login_home(driver, config)
    def login_service_point(self, driver, config): login_service_point(driver, config)
    def daypart_activity(self, driver, config, date): daypart_activity(driver, config, date)
    def sales_activity(self, driver, config, date): sales_activity(driver, config, date)
    def cem_report_builder(self, driver, config): cem_report_builder(driver, config)
    def catering_orders(self, driver, config, date): catering_orders(driver, config, date)