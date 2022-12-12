from ._catering_for_slack_groupme import catering_for_slack_groupme
from ._cems_for_slack_groupme import cems_for_slack_groupme
from ._faith import faith


class messages:
    def __init__(self):
        pass

    def catering_for_slack_groupme(self, date, data): return catering_for_slack_groupme(date, data)
    def cems_for_slack_groupme(self, data): return cems_for_slack_groupme(data)
    def faith(self, engine): return faith()