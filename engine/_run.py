import sys

def run(self):
 
    # run at 6AM each day
    if sys.argv[1] == 'southroads-reports': self.routes.cfa.southroads_reports(self)

    # need to adjust so only sales reports are deleted upon single day selection
    if sys.argv[1] == 'sales': self.routes.gforms.track_southroads_sales(self)


    if sys.argv[1] == 'cem': 
        if sys.argv[2] == '-slack': self.routes.slack.southroads_cem_script(self)
        if sys.argv[2] == '-groupme': self.routes.groupme.southroads_cem_script(self)
    
    
    if sys.argv[1] == 'catering': 
        if sys.argv[2] == '-slack': self.routes.slack.southroads_catering_script(self)
        if sys.argv[2] == '-groupme': self.routes.groupme.southroads_catering_script(self)
        




        