import sys

def run(self):

    # previous days sales
    if sys.argv[1] == '-s':
        
        # checking for proper input
        if len(sys.argv) != 3:
            print('Usage Example: python3 main.py -s 11/21/2022')
        
        # running script
        if len(sys.argv) == 3:
            date = sys.argv[2]
            self.init_script()
            self.routes.login_cfa_home(self)
            self.routes.login_service_point(self)
            # self.routes.daypart_activity(self, date)
            # self.routes.extract_daypart_activity(self)
            self.routes.sales_activity(self, date)
            # self.routes.log_sales_data(self)
            # self.driver.close()

    # current month CEMS
    if sys.argv[1] == '-c':
        self.routes.cem_report_builder(self)
        self.routes.extract_cem_scores(self)

    # testing scripts
    if sys.argv[1] == '-t':
        # self.routes.login_service_point(self)
        # self.routes.daypart_activity(self)
        self.routes.extract_daypart_activity(self)
        print(self.data.sales_data)
        