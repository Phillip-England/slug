import os
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

def login(driver, config, account):

    username_id = 'signinUserNameInput'
    password_id = 'signinPasswordInput'

    driver.get(os.environ.get("GROUPME_LOGIN_PAGE"))

    username_input = WebDriverWait(driver, config.max_wait_time).until(expected_conditions.visibility_of_element_located((By.ID, username_id)))

    password_input = driver.find_element(By.ID, password_id)   
    
    username_input.send_keys(account.get('username'))
    password_input.send_keys(account.get('password'))


    password_input.submit()