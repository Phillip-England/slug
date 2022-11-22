from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import pyautogui

import os
import time


def login_service_point(engine):

    # entering login info (cookies will be generated upon login)
    try:
        engine.driver.get(engine.config.service_point_url)
        service_point_login_input = WebDriverWait(engine.driver, engine.config.max_wait_time).until(expected_conditions.visibility_of_element_located((By.ID, engine.config.service_point_login_input_id)))   
        service_point_login_input.send_keys(os.environ.get('SERVICE_POINT_LOGIN'))
        print(f"Login info entered at {engine.config.service_point_url}")
    except:
        raise Exception(f"Failed to enter login info at {engine.config.service_point_url}")
    
    # submitting login info
    try:
        service_point_submit = WebDriverWait(engine.driver, engine.config.max_wait_time).until(expected_conditions.visibility_of_element_located((By.ID, engine.config.service_point_submit_id)))  
        service_point_submit.click()
        print(f"Login info submitted {engine.config.service_point_url}")
    except:
        raise Exception(f"Failed to submit login info at {engine.config.service_point_url}")

    # clearing end of day alert and checking if page is loaded
    try:
        time.sleep(1)
        pyautogui.press('enter')
        service_point_make_favorite_button = WebDriverWait(engine.driver, engine.config.max_wait_time).until(expected_conditions.visibility_of_element_located((By.ID, engine.config.service_point_make_favorite_button_id)))
        print(f"Page loaded at {engine.config.service_point_url}")
    except:
        raise Exception(f'Page failed to load at {engine.config.service_point_url}')
