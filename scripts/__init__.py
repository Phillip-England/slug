
from ._track_previous_day_sales import track_previous_day_sales
from ._send_daily_slack_message import send_daily_slack_message
from ._send_faith_message import send_faith_message

class scripts:
    def __init__(self):
        pass

    def track_previous_day_sales(self, engine): track_previous_day_sales(engine)
    def send_daily_slack_message(self, engine): send_daily_slack_message(engine)
    def send_faith_message(self, engine): send_faith_message(engine)