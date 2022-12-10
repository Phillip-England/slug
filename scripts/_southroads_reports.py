def southroads_reports(engine):
    yesterday_unformatted = engine.date.get_past_date(1)
    yesterday_formatted = engine.date.format_date(yesterday_unformatted, 'x/x/xxxx')
    engine.directories.clear_downloads(engine)
    engine.driver.maximize_window()
    engine.routes.login_cfa_home(engine)
    engine.routes.cem_report_builder(engine)
    engine.routes.login_service_point(engine)
    engine.routes.daypart_activity(engine, yesterday_formatted)
    engine.routes.sales_activity(engine, yesterday_formatted)
    engine.routes.deferred_orders(engine, yesterday_formatted)
    