import os
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

def login(self, driver, config, account):



    driver.get(os.environ.get("GROUPME_LOGIN_PAGE"))

    username_input = WebDriverWait(driver, config.max_wait_time).until(expected_conditions.visibility_of_element_located((By.ID, self.login_username_id)))

    password_input = driver.find_element(By.ID, self.login_password_id)   
    
    username_input.send_keys(account.get('username'))
    password_input.send_keys(account.get('password'))


    password_input.submit()