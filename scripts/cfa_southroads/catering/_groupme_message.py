
def groupme_message(engine):

    engine.driver.maximize_window()

    engine.data.extract_deferred_orders(engine.config)
    message = engine.messages.catering_for_slack_groupme(engine.date, engine.data)

    if engine.config.testing_groupme == True:
        engine.routes.groupme.login(engine.driver, engine.config, engine.routes.groupme.testing_account)
        engine.routes.groupme.send_message(engine.driver, engine.config, engine.routes.groupme.testing_account, message)
    else:
        engine.routes.groupme.login(engine.driver, engine.config, engine.routes.groupme.southroads_account)
        engine.routes.groupme.send_message(engine.driver, engine.config, engine.routes.groupme.southroads_account, message)
