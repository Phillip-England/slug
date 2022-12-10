import sys

def run(self):
    if sys.argv[1] == 'sales': self.scripts.track_previous_day_sales(self)
    if sys.argv[1] == 'slack': self.scripts.send_daily_slack_message(self)
    if sys.argv[1] == 'faith': self.scripts.send_faith_message(self)
    if sys.argv[1] == 'catering': self.scripts.send_next_day_catering_group_me(self)




        