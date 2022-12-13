from ._groupme_message import groupme_message
from ._slack_message import slack_message
from ._slack_schedule_message import slack_schedule_message

class catering:

    def __init__(self):
        pass

    def groupme_message(self, engine): groupme_message(engine)
    def slack_message(self, engine): slack_message(engine)
    def slack_schedule_message(self, engine): slack_schedule_message(engine)