import os
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

def login_groupme(engine):

    engine.driver.get(os.environ.get("GROUPME_LOGIN_PAGE"))

    username_input = WebDriverWait(engine.driver, engine.config.max_wait_time).until(expected_conditions.visibility_of_element_located((By.ID, engine.config.groupme_username_id)))

    password_input = engine.driver.find_element(By.ID, engine.config.groupme_password_id)   
    
    if engine.config.testing_groupme == True:
        username_input.send_keys(os.environ.get("GROUPME_TESTING_USERNAME"))
        password_input.send_keys(os.environ.get("GROUPME_TESTING_PASSWORD"))
    else:
        username_input.send_keys(os.environ.get("GROUPME_USERNAME"))
        password_input.send_keys(os.environ.get("GROUPME_PASSWORD"))


    password_input.submit()