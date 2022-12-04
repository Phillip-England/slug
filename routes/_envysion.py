import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import time
import pyautogui

def envysion(engine):

    try:
    
        engine.driver.get(os.environ.get("ENVYSION_HOMEPAGE"))

        envysion_email_input = WebDriverWait(engine.driver, engine.config.max_wait_time).until(expected_conditions.visibility_of_element_located((By.ID, engine.config.envysion_email_input_id)))

        envysion_email_input.send_keys(os.environ.get('CFA_EMAIL'))
        time.sleep(0.2)

        pyautogui.press('enter')

        envysion_password_input = WebDriverWait(engine.driver, engine.config.max_wait_time).until(expected_conditions.visibility_of_element_located((By.ID, engine.config.envysion_password_input_id)))
        time.sleep(0.2)

        envysion_password_input.send_keys(os.environ.get("ENVYSION_PASSWORD"))

        pyautogui.press('enter')

        envysion_loading_element = WebDriverWait(engine.driver, engine.config.max_wait_time).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, engine.config.envysion_loading_element_class_name)))

        engine.driver.get(os.environ.get("ENVYSION_FRONT_COUNTER_OVERVIEW"))



    except Exception as error:
        engine.driver.close()
        raise SystemExit(error)