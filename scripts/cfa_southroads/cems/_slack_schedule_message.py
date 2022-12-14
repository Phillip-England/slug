import os

def slack_schedule_message(engine):

    engine.data.extract_cem_scores(engine.config)

    message = engine.messages.cems_for_slack_groupme(engine.data)

    if engine.config.testing_slack == True:
        engine.routes.slack.login(engine.driver, engine.config, engine.routes.slack.testing_account)
        engine.routes.slack.schedule_message(engine.driver, engine.config, engine.routes.slack.testing_account, message)
    else:
        engine.routes.slack.login(engine.driver, engine.config, engine.routes.slack.southroads_account)
        engine.routes.slack.schedule_message(engine.driver, engine.config, engine.routes.slack.southroads_account, message)

    engine.driver.close()

