from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import pyautogui

import os
import time


def login_service_point(self, driver, config):

    driver.get(self.service_point_url)
    login_input = WebDriverWait(driver, config.max_wait_time).until(expected_conditions.visibility_of_element_located((By.ID, self.service_point_login_input_id)))   
    login_input.send_keys(os.environ.get('SERVICE_POINT_LOGIN'))
    
    submit = WebDriverWait(driver, config.max_wait_time).until(expected_conditions.visibility_of_element_located((By.ID, self.service_point_submit_id)))  
    submit.click()

    time.sleep(1)
    pyautogui.press('enter')
    favorite_button = WebDriverWait(driver, config.max_wait_time).until(expected_conditions.visibility_of_element_located((By.ID, self.service_point_favorite_button_id)))
