import os
import logging
logger = logging.getLogger()
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

def login_cfa_home(engine):

    #going to cfahome (once we login the cookies will persist for the lifetime of the chrome driver)
    engine.driver.get(engine.config.cfa_home_url)

    #entering username info
    try:
        cfa_username_input = WebDriverWait(engine.driver, engine.config.max_wait_time).until(expected_conditions.visibility_of_element_located((By.ID, engine.config.cfa_username_input_id)))   
        cfa_username_input.send_keys(os.environ.get('CFA_USERNAME'))
        cfa_username_input.submit()
        print(f"username successfully submitted at {engine.config.cfa_home_url}")
    except:
        raise Exception(f'Failed to enter username info at {engine.config.cfa_home_url}')

    #entering password info
    try:
        cfa_password_input = WebDriverWait(engine.driver, engine.config.max_wait_time).until(expected_conditions.visibility_of_element_located((By.ID, engine.config.cfa_password_input_id)))
        cfa_password_input.send_keys(os.environ.get('CFA_PASSWORD'))
        cfa_password_input.submit() # auth cookies are set here
        print(f"password successfully submitted at {engine.config.cfa_home_url}")
    except:
        raise Exception(f'Failed to enter password info at {engine.config.cfa_home_url}')

    #waiting for site to be fully loaded
    try:
        reports_and_tools_dropdown = WebDriverWait(engine.driver, engine.config.max_wait_time).until(expected_conditions.visibility_of_element_located((By.ID, engine.config.cfa_reports_and_tools_dropdown_id))) 
        print(f"Page loaded at {engine.config.cfa_home_url}")
    except:
        raise Exception(f'{engine.config.cfa_home_url} failed to fully load after successfully submitting login info')