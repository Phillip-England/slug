
# class methods
from ._login_cfa_home import login_cfa_home
from ._login_service_point import login_service_point
from ._daypart_activity import daypart_activity
from ._extract_daypart_activity import extract_daypart_activity
from ._log_sales_data import log_sales_data
from ._cem_report_builder import cem_report_builder
from ._extract_cem_scores import extract_cem_scores

class routes:
    def __init__(self):
        pass

    def login_cfa_home(self, engine): login_cfa_home(engine)
    def login_service_point(self, engine): login_service_point(engine)
    def daypart_activity(self, engine, start_date, end_date): daypart_activity(engine, start_date, end_date)
    def extract_daypart_activity(self, engine): extract_daypart_activity(engine)
    def log_sales_data(self, engine): log_sales_data(engine)
    def cem_report_builder(self, engine): cem_report_builder(self, engine)
    def extract_cem_scores(self, engine): extract_cem_scores(self, engine)