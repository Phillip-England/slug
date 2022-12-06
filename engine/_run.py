import sys

def run(self):

    # previous days sales
    if sys.argv[1] == '-s':
        
        # checking for proper input
        if len(sys.argv) != 3:
            print('Usage Example: python3 main.py -s 11/21/2022')
        
        # running script
        if len(sys.argv) == 3:
            print("Selected sales script")
            date = sys.argv[2]
            self.init_script()
            self.routes.login_cfa_home(self)
            self.routes.login_service_point(self)
            self.routes.daypart_activity(self, date)
            self.data.extract_daypart_activity(self)
            self.routes.sales_activity(self, date)
            self.data.extract_sales_activity(self)
            self.routes.log_sales_data(self)
            self.driver.close()
            print(vars(self.data))

    # current month CEMS
    if sys.argv[1] == '-cem':
        print('Selected CEM script')
        self.init_script()
        # self.routes.login_cfa_home(self)
        # self.routes.cem_report_builder(self)
        self.data.extract_cem_scores(self)
        self.routes.slack_message(self, self.data.get_cem_message())
        self.data.print_cems()
        self.driver.close()

    # testing scripts
    if sys.argv[1] == '-t':
        self.init_script()
        self.routes.envysion(self)




        