def sales(engine):
    yesterday = engine.date.format_date(engine.date.get_past_date(1), 'x/x/xxxx')
    engine.directories.delete_file(engine.directories.downloads, engine.directories.sales_activity_download_path)
    engine.directories.delete_file(engine.directories.downloads, engine.directories.daypart_activity_download_path)
    engine.driver.maximize_window()
    engine.routes.cfa.login_home(engine.driver, engine.config)
    engine.routes.cfa.login_service_point(engine.driver, engine.config)
    engine.routes.cfa.daypart_activity(engine.driver, engine.config, yesterday)
    engine.routes.cfa.sales_activity(engine.driver, engine.config, yesterday)



    