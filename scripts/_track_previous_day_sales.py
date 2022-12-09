def track_previous_day_sales(engine):
        engine.directories.clear_downloads()
        engine.driver.maximize_window()
        yesterday_unformatted = engine.date.get_past_date(1)
        yesterday_formatted = engine.date.format_date(yesterday_unformatted, 'x/x/xxxx')
        engine.routes.login_cfa_home(engine)
        engine.routes.login_service_point(engine)
        engine.routes.daypart_activity(engine, yesterday_formatted)
        engine.data.extract_daypart_activity(engine)
        engine.routes.sales_activity(engine, yesterday_formatted)
        engine.data.extract_sales_activity(engine)
        engine.routes.log_sales_data(engine)
        engine.driver.close()
        print(vars(engine.data))