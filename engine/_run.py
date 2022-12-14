import sys

def run(self):
 
    # run at 6AM each day
    if sys.argv[1] == 'southroads-reports': 
        if sys.argv[2] == '-all': self.scripts.cfa_southroads.reports.get_all(self)
        if sys.argv[2] == '-catering': self.scripts.cfa_southroads.reports.catering(self)
        if sys.argv[2] == '-sales': self.scripts.cfa_southroads.reports.sales(self)
        if sys.argv[2] == '-cems': self.scripts.cfa_southroads.reports.cems(self)
        if sys.argv[2] == '-bday': self.scripts.cfa_southroads.reports.bday(self)

    if sys.argv[1] == 'track': 
        if sys.argv[2] == '-sales': self.scripts.cfa_southroads.tracking.sales(self)

    if sys.argv[1] == 'cems': 
        if sys.argv[2] == '-slack': self.scripts.cfa_southroads.cems.slack_message(self)
        if sys.argv[2] == '-groupme': self.scripts.cfa_southroads.cems.groupme_message(self)
    
    
    if sys.argv[1] == 'catering': 
        if sys.argv[2] == '-slack': self.scripts.cfa_southroads.catering.slack_message(self)
        if sys.argv[2] == '-groupme': self.scripts.cfa_southroads.catering.groupme_message(self)
        




        