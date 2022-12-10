import os
import sys

def cem_message(engine):

    engine.driver.maximize_window()
    engine.data.extract_cem_scores(engine)

    if engine.config.testing_slack == True:
        engine.routes.login_slack(engine, os.environ.get("SLACK_TESTING_LOGIN_PAGE"))
    else:
        engine.routes.login_slack(engine, os.environ.get("SLACK_LOGIN_PAGE"))
        

    # message = engine.messages.cems_for_slack_groupme(engine)
    # print(message)
    # engine.routes.slack_message(engine, engine.data.get_slack_message(engine))

