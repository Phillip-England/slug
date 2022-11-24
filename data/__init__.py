from ._extract_daypart_activity import extract_daypart_activity
from ._extract_cem_scores import extract_cem_scores
from ._extract_sales_activity import extract_sales_activity

class data:
    def __init__(self):
        pass
        # date
        # day
        # breakfast_sales
        # breakfast_transactions
        # breakfast_check_average
        # lunch_sales
        # lunch_transactions
        # lunch_check_average
        # midshift_sales
        # midshift_transactions
        # midshift_check_average
        # dinner_sales
        # dinner_transactions
        # dinner_check_average
        # carryout_sales
        # cfa_delivery_sales
        # delivery_sales
        # dine_in_sales
        # drive_thru_sales
        # m_carryout_sales
        # m_dine_in_sales
        # m_drive_thru_sales
        # on_demand_sales
        # pickup_sales


    def set_current_month_cem_data(self, data_dictionary):
        self.current_month_cem_data = data_dictionary

    def extract_daypart_activity(self, engine): extract_daypart_activity(engine)
    def extract_cem_scores(self, engine): extract_cem_scores(engine)
    def extract_sales_activity(self, engine): extract_sales_activity(engine)