import sys

def run(self):
 
    # run at 6AM each day
    if sys.argv[1] == 'southroads-reports': self.scripts.southroads_reports(self)

    # need to adjust so only sales reports are deleted upon single day selection
    if sys.argv[1] == 'sales': self.scripts.track_southroads_sales(self)


    if sys.argv[1] == 'cem': self.scripts.cem_message(self)
    if sys.argv[1] == 'faith': self.scripts.faith_message(self)
    if sys.argv[1] == 'catering': self.scripts.catering_message(self)




        