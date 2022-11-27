from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import time

def log_cem_data(engine):

    try:
    
        # loading the google form
        engine.driver.get(engine.config.cem_tracking_form_url)
        loading_element = WebDriverWait(engine.driver, engine.config.max_wait_time).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, engine.config.cem_tracking_loading_element)))
        inputs = engine.driver.find_elements(By.CLASS_NAME, engine.config.cem_tracking_inputs_class_name)
        submit = engine.driver.find_elements(By.CLASS_NAME, engine.config.cem_tracking_submit_button)
        print(f'Page loaded at {engine.driver.current_url}')

        # breaking out our inputs and submit button
        submit_button = submit[0]
        date_input = inputs[0]
        day_input = inputs[1]
        surveys_input = inputs[2]
        osat_input = inputs[3]
        taste_input = inputs[4]
        speed_input = inputs[5]
        ace_input = inputs[6]
        cleanliness_input = inputs[7]
        accuracy_input = inputs[8]

        # sending in data
        date_input.send_keys(engine.data.date)
        day_input.send_keys(engine.data.day_of_week)
        surveys_input.send_keys(engine.data.number_of_surveys)
        osat_input.send_keys(engine.data.osat)
        taste_input.send_keys(engine.data.taste)
        speed_input.send_keys(engine.data.speed)
        ace_input.send_keys(engine.data.ace)
        cleanliness_input.send_keys(engine.data.cleanliness)
        accuracy_input.send_keys(engine.data.accuracy)
        submit_button.click()
        print(f'CEM scores logged at {engine.driver.current_url}')
        time.sleep(3)

    except Exception as error:
        engine.driver.close()
        raise SystemExit(error)



