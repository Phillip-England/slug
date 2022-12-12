from routes import slack
from routes import cfa
from routes import groupme
from routes import gforms


class routes:
    def __init__(self):
        self.slack = slack.slack()
        self.cfa = cfa.cfa()
        self.groupme = groupme.groupme()
        self.gforms = gforms.gforms()
