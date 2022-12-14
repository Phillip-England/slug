import os


def get(engine):
    engine.routes.cfa.login_home(engine.driver, engine.config)
    engine.routes.cfa.hr_payroll(engine.driver, engine.config, engine.date)