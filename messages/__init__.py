from ._catering_for_slack_groupme import catering_for_slack_groupme
from ._cems_for_slack_groupme import cems_for_slack_groupme
from ._faith import faith


class messages:
    def __init__(self):
        pass

    def catering_for_slack_groupme(self, engine, deferred_orders): return catering_for_slack_groupme(engine, deferred_orders)
    def cems_for_slack_groupme(self, engine): return cems_for_slack_groupme(engine)
    def faith(self, engine): return faith()