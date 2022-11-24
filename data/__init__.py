from ._extract_daypart_activity import extract_daypart_activity
from ._extract_cem_scores import extract_cem_scores
from ._extract_sales_activity import extract_sales_activity

class data:
    def __init__(self):
        pass
        #current_month_cem_data
        #sales_data

    def set_current_month_cem_data(self, data_dictionary):
        self.current_month_cem_data = data_dictionary

    def set_previous_business_day_sales_data(self, data_dictionary):
        self.previous_business_day_sales_data = data_dictionary

    def extract_daypart_activity(self, engine): extract_daypart_activity(engine)
    def extract_cem_scores(self, engine): extract_cem_scores(engine)
    def extract_sales_activity(self, engine): extract_sales_activity(engine)