import os
import sys

def send_daily_slack_message(engine):

    if sys.argv[2] == '-cem':
        engine.directories.clear_downloads()
        engine.driver.maximize_window()
        yesterday_unformatted = engine.date.get_past_date(1)
        yesterday_formatted = engine.date.format_date(yesterday_unformatted, 'x/x/xxxx')
        engine.routes.login_cfa_home(engine)
        engine.routes.cem_report_builder(engine)
        engine.data.extract_cem_scores(engine)
        engine.routes.slack_message(engine, engine.data.get_slack_message(engine))
        print(vars(engine.data))

    
    if sys.argv[2] == '-all':
        engine.directories.clear_downloads()
        engine.driver.maximize_window()
        yesterday_unformatted = engine.date.get_past_date(1)
        yesterday_formatted = engine.date.format_date(yesterday_unformatted, 'x/x/xxxx')
        engine.init_script()
        engine.routes.login_cfa_home(engine)
        engine.routes.cem_report_builder(engine)
        engine.routes.login_service_point(engine)
        engine.routes.daypart_activity(engine, yesterday_formatted)
        engine.routes.sales_activity(engine, yesterday_formatted)
        engine.data.extract_sales_activity(engine)
        engine.data.extract_cem_scores(engine)
        engine.data.extract_daypart_activity(engine)
        engine.routes.slack_message(engine, engine.data.get_slack_message(engine))
        print(vars(engine.data))
