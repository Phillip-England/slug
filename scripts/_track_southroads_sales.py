import sys

def track_southroads_sales(engine):

        # if you feed the program -p it will log the previous days sales
        # otherwise, you need to specify the exact date in 'x/x/xxxx' format
        
        if sys.argv[2] == '-p':
                engine.driver.maximize_window()
                engine.data.extract_daypart_activity(engine)
                engine.data.extract_sales_activity(engine)
                engine.routes.log_sales_data(engine)
                engine.driver.close()
        else:
                selected_date = sys.argv[2]
                engine.directories.clear_downloads(engine)
                engine.driver.maximize_window()
                engine.routes.login_cfa_home(engine)
                engine.routes.login_service_point(engine)
                engine.routes.daypart_activity(engine, selected_date)
                engine.data.extract_daypart_activity(engine)
                engine.routes.sales_activity(engine, selected_date)
                engine.data.extract_sales_activity(engine)
                engine.routes.log_sales_data(engine)
                engine.driver.close()