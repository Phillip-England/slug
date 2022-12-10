import os
import time
import pyautogui
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

def deferred_orders(engine, business_date):

    engine.driver.get(os.environ.get('DEFERRED_ORDER_REPORT'))

    start_date = WebDriverWait(engine.driver, engine.config.max_wait_time).until(expected_conditions.visibility_of_element_located((By.ID, engine.config.deferred_start_date_id)))  

    end_date = engine.driver.find_element(By.ID, engine.config.deferred_end_date_id)

    submit = engine.driver.find_element(By.ID, engine.config.deferred_submit_id)

    start_date.click()
    time.sleep(2)
    pyautogui.press('backspace', presses=10)
    start_date.send_keys(business_date)

    end_date.click()
    time.sleep(2)
    pyautogui.press('backspace', presses=10)
    end_date.send_keys(business_date)

    time.sleep(5)

    submit.click()

    time.sleep(5)
