from ._login import login
from ._message import message

class groupme:

    def __init__(self):
        pass

    def login(self, driver, config): login(driver, config)
    def message(self, driver, config): message(driver, config)