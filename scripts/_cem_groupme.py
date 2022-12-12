import os

def cem_groupme(engine):

    engine.driver.maximize_window()
    engine.data.extract_cem_scores(engine.config)

    message = engine.messages.cems_for_slack_groupme(engine.data)

    if engine.config.testing_groupme == True:
        engine.routes.groupme.login(engine.driver, engine.config, engine.routes.groupme.testing_account)
        engine.routes.groupme.send_message(engine.driver, engine.config, engine.routes.groupme.testing_account, message)
    else:
        engine.routes.groupme.login(engine.driver, engine.config, engine.routes.groupme.southroads_account)
        engine.routes.groupme.send_message(engine.driver, engine.config, engine.routes.groupme.southroads_account, message)


    engine.driver.close()