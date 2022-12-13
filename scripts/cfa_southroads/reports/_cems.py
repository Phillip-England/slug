def cems(engine):
    engine.directories.delete_file(engine.directories.downloads, engine.directories.cem_current_month_download_path)
    engine.directories.delete_file(engine.directories.downloads, engine.directories.cem_ninty_day_rolling_download_path)
    engine.directories.delete_file(engine.directories.downloads, engine.directories.cem_year_to_date_download_path)
    engine.driver.maximize_window()
    engine.routes.cfa.login_home(engine.driver, engine.config)
    engine.routes.cfa.cem_report_builder(engine.driver, engine.config)
    engine.driver.close()