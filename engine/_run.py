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
            self.routes.daypart_activity(self, date)
            self.data.extract_daypart_activity(self)
            self.routes.sales_activity(self, date)
            self.data.extract_sales_activity(self)
            self.routes.log_sales_data(self)
            self.driver.close()
            print(vars(self.data))

    # current month CEMS
    if sys.argv[1] == '-cem':

        # picked a specific date
        if len(sys.argv) == 3 and sys.argv[2] != '-cm' and sys.argv[2] != '-ytd' and sys.argv[2] != '-ndr':
            print('Selected Specific Day for CEM Script')
            keyword = sys.argv[2]
            self.init_script()
            self.routes.login_cfa_home(self)
            self.routes.cem_report_builder(self, keyword)
            self.data.extract_cem_scores(self)
            self.routes.log_cem_data(self)
            self.driver.close()
            print(vars(self.data))

        # picked cm
        if len(sys.argv) == 3 and sys.argv[2] == '-cm':
            print("Selected Current Month for CEM Script")
            keyword = sys.argv[2]
            self.init_script()
            self.routes.login_cfa_home(self)
            self.routes.cem_report_builder(self, keyword)
            self.data.extract_cem_scores(self, keyword)
            self.driver.close()
            print(vars(self.data))

        # picked ndr
        if len(sys.argv) == 3 and sys.argv[2] == '-ndr':
            print("Selected Ninty Day Rolling for CEM Script")
            keyword = sys.argv[2]
            self.init_script()
            self.routes.login_cfa_home(self)
            self.routes.cem_report_builder(self, keyword)
            self.data.extract_cem_scores(self, keyword)
            self.driver.close()
            print(vars(self.data))


    # testing scripts
    if sys.argv[1] == '-t':
        self.init_script()
        self.driver.close()
        self.data.extract_cem_scores(self)
        print(vars(self.data))

        