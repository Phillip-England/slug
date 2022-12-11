import sys

def track_southroads_sales(engine):
        engine.driver.maximize_window()
        engine.data.extract_daypart_activity(engine.config)
        engine.data.extract_sales_activity(engine.config)
        engine.routes.gforms.sales_data(engine.driver, engine.config, engine.data)
        engine.driver.close()