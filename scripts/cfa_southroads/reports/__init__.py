from ._get_all import get_all
from ._catering import catering
from ._sales import sales
from ._cems import cems

class reports:

    def __init__(self):
        pass

    def get_all(self, engine): get_all(engine)
    def catering(self, engine): catering(engine)
    def sales(self, engine): sales(engine)
    def cems(self, engine): cems(engine)