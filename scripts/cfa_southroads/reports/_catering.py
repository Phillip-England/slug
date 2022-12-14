

def catering(engine):
    tomorrow = engine.date.format_date(engine.date.get_future_date(1), 'x/x/xxxx')
    engine.directories.delete_file(engine.directories.downloads, engine.directories.catering_download_path)
    engine.routes.cfa.login_home(engine.driver, engine.config)
    engine.routes.cfa.login_service_point(engine.driver, engine.config)
    engine.routes.cfa.catering_orders(engine.driver, engine.config, tomorrow)
    engine.driver.close()