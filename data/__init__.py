from ._extract_daypart_activity import extract_daypart_activity
from ._extract_cem_scores import extract_cem_scores
from ._extract_sales_activity import extract_sales_activity
from ._extract_cem_spreadsheet_data import extract_cem_spreadsheet_data
from ._print_cems import print_cems
from ._get_slack_message import get_slack_message
from ._get_random_faith_message import get_random_faith_message

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
        # total_sales
        # total_transactions
        # total_check_average
        # carryout_sales
        # cfa_delivery_sales
        # curbside sales
        # delivery_sales
        # dine_in_sales
        # drive_thru_sales
        # m_carryout_sales
        # m_dine_in_sales
        # m_drive_thru_sales
        # on_demand_sales
        # pickup_sales
        # found_yesterday_daypart_activity
        # found_yesterday_sales_activity
        # number_of_surveys
        # osat
        # taste
        # speed
        # ace
        # cleanliness
        # accuracy
        # ninty_day_survey_list
        # ninty_day_day_of_week_list
        # ninty_day_osat_list
        # ninty_day_taste_list
        # ninty_day_speed_list
        # ninty_day_ace_list
        # ninty_day_cleanliness_list
        # ninty_day_accuracy_list
        # current_month_survey_list
        # current_month_day_of_week
        # current_month_osat_list
        # current_month_taste_list
        # current_month_speed_list
        # current_month_ace_list
        # current_month_cleanliness_list
        # current_month_accuracy_list


    def extract_daypart_activity(self, engine): extract_daypart_activity(engine)
    def extract_cem_scores(self, engine): extract_cem_scores(engine)
    def extract_sales_activity(self, engine): extract_sales_activity(engine)
    def extract_cem_spreadsheet_data(self, engine): extract_cem_spreadsheet_data(engine)
    def print_cems(self): print_cems(self)
    def get_slack_message(self, engine): return get_slack_message(engine)
    def get_random_faith_message(self, engine): return get_random_faith_message(engine)

