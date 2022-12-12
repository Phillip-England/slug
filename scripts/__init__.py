
from ._track_southroads_sales import track_southroads_sales
from ._cem_slack import cem_slack
from ._cem_groupme import cem_groupme
from ._faith_message import faith_message
from ._catering_slack import catering_slack
from ._southroads_reports import southroads_reports
from ._catering_groupme import catering_groupme

class scripts:
    def __init__(self):
        pass

    def southroads_reports(self, engine): southroads_reports(engine)
    def track_southroads_sales(self, engine): track_southroads_sales(engine)
    def cem_slack(self, engine): cem_slack(engine)
    def cem_groupme(self, engine): cem_groupme(engine)
    def faith_message(self, engine): faith_message(engine)
    def catering_slack(self, engine): catering_slack(engine)
    def catering_groupme(self, engine): catering_groupme(engine)