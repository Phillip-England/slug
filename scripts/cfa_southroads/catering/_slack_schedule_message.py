
def slack_schedule_message(engine):

    engine.data.extract_deferred_orders(engine.config)
    message = engine.messages.catering_for_slack_groupme(engine.date, engine.data)

    if engine.config.testing_slack == True:
        engine.routes.slack.login(engine.driver, engine.config, engine.routes.slack.testing_account)
        engine.routes.slack.schedule_message(engine.driver, engine.config, engine.routes.slack.testing_account, message)
    else:
        engine.routes.slack.login(engine.driver, engine.config, engine.routes.slack.southroads_account)
        engine.routes.slack.schedule_message(engine.driver, engine.config, engine.routes.slack.southroads_account, message)
