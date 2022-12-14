import scripts.cfa_southroads.catering as catering
import scripts.cfa_southroads.cems as cems
import scripts.cfa_southroads.reports as reports
import scripts.cfa_southroads.tracking as tracking
import scripts.cfa_southroads.bday as bday

class cfa_southroads:

    def __init__(self):
        self.catering = catering.catering()
        self.cems = cems.cems()
        self.reports = reports.reports()
        self.tracking = tracking.tracking()
        self.bday = bday.bday()


