import sys
import time
import os

def run(self):
    if sys.argv[1] == 'sales': self.scripts.track_previous_day_sales(self)
    if sys.argv[1] == 'slack': self.scripts.send_daily_slack_message(self)
    if sys.argv[1] == 'faith': self.scripts.send_faith_message(self)




        