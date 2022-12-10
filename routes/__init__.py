
# class methods
from ._login_cfa_home import login_cfa_home
from ._login_service_point import login_service_point
from ._daypart_activity import daypart_activity
from ._sales_activity import sales_activity
from ._log_sales_data import log_sales_data
from ._cem_report_builder import cem_report_builder
from ._log_cem_data import log_cem_data
from ._cem_spreadsheet import cem_spreadsheet
from ._slack_message import slack_message
from ._envysion import envysion
from ._deferred_orders import deferred_orders
from ._login_groupme import login_groupme
from ._groupme_message import groupme_message

class routes:
    def __init__(self):
        pass

    def login_cfa_home(self, engine): login_cfa_home(engine)
    def login_service_point(self, engine): login_service_point(engine)
    def daypart_activity(self, engine, date): daypart_activity(engine, date)
    def sales_activity(self, engine, date): sales_activity(engine, date)
    def log_sales_data(self, engine): log_sales_data(engine)
    def cem_report_builder(self, engine): cem_report_builder(engine)
    def log_cem_data(self, engine): log_cem_data(engine)
    def cem_spreadsheet(self, engine): cem_spreadsheet(engine)
    def slack_message(self, engine, message): slack_message(engine, message)
    def envysion(self, engine): envysion(engine)
    def deferred_orders(self, engine, business_date): deferred_orders(engine, business_date)
    def login_groupme(self, engine): login_groupme(engine)
    def groupme_message(self, engine, message): groupme_message(engine, message)