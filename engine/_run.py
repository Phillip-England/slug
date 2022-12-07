import sys
import time

def run(self):

    # previous days sales
    if sys.argv[1] == '-sales':
                
        print("Selected sales script")
        yesterday_unformatted = self.date.get_past_date(1)
        yesterday_formatted = self.date.format_date(yesterday_unformatted, 'x/x/xxxx')
        self.init_script()
        self.routes.login_cfa_home(self)
        self.routes.login_service_point(self)
        self.routes.daypart_activity(self, yesterday_formatted)
        self.data.extract_daypart_activity(self)
        self.routes.sales_activity(self, yesterday_formatted)
        self.data.extract_sales_activity(self)
        self.routes.log_sales_data(self)
        self.driver.close()
        print(vars(self.data))

    # current month CEMS
    if sys.argv[1] == '-cem':
        print('Selected CEM script')
        self.init_script()
        self.routes.login_cfa_home(self)
        self.routes.cem_report_builder(self)
        self.data.extract_cem_scores(self)
        self.routes.slack_message(self, self.data.get_cem_message())
        self.data.print_cems()
        self.driver.close()

    if sys.argv[1] == '-slack':
        print("Selected slack reporting script")
        # yesterday_unformatted = self.date.get_past_date(1)
        # yesterday_formatted = self.date.format_date(yesterday_unformatted, 'x/x/xxxx')
        self.init_script()
        self.routes.login_cfa_home(self)
        self.routes.cem_report_builder(self)
        self.routes.login_service_point(self)
        self.routes.daypart_activity(self, '12/4/2022')
        self.routes.sales_activity(self, '12/4/2022')

        if self.data.found_yesterday_daypart_activity == True and self.data.found_yesterday_sales_activity == True:
            self.routes.log_sales_data(self)


        self.data.extract_sales_activity(self)
        self.data.extract_cem_scores(self)
        self.data.extract_daypart_activity(self)
        self.routes.slack_message(self, self.data.get_slack_message())
        print(vars(self.data))




    # testing scripts
    if sys.argv[1] == '-t':
        self.init_script()
        self.routes.envysion(self)




        