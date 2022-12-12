import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

def login_home(self, driver, config):

    driver.get(self.cfahome_url)

    username_input = WebDriverWait(driver, config.max_wait_time).until(expected_conditions.visibility_of_element_located((By.ID, self.login_username_id)))   
    username_input.send_keys(os.environ.get('CFA_USERNAME'))
    username_input.submit()

    password_input = WebDriverWait(driver, config.max_wait_time).until(expected_conditions.visibility_of_element_located((By.ID, self.login_password_id)))
    password_input.send_keys(os.environ.get('CFA_PASSWORD'))
    password_input.submit()

    reports_and_tools_dropdown = WebDriverWait(driver, config.max_wait_time).until(expected_conditions.visibility_of_element_located((By.ID, self.homepage_reports_id))) 