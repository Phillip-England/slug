from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import pyautogui

import os
import time


def login_service_point(driver, config):

    service_point_url = os.environ.get("SERVICE_POINT_URL")
    login_input_id = 'MainContent_txtEchoWindow'
    submit_id = 'MainContent_btnEnter'
    favorite_button_id = 'btnMakeFavorite'

    driver.get(service_point_url)
    login_input = WebDriverWait(driver, config.max_wait_time).until(expected_conditions.visibility_of_element_located((By.ID, login_input_id)))   
    login_input.send_keys(os.environ.get('SERVICE_POINT_LOGIN'))
    
    submit = WebDriverWait(driver, config.max_wait_time).until(expected_conditions.visibility_of_element_located((By.ID, submit_id)))  
    submit.click()

    time.sleep(1)
    pyautogui.press('enter')
    favorite_button = WebDriverWait(driver, config.max_wait_time).until(expected_conditions.visibility_of_element_located((By.ID, favorite_button_id)))
