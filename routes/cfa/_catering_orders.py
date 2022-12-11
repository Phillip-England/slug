import os
import time
import pyautogui
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

def catering_orders(driver, config, date):

    catering_order_url = os.environ.get('DEFERRED_ORDER_REPORT')
    start_date_id = 'MainContent_BusDate1_I'
    end_date_id = 'MainContent_BusDate2_I'
    submit_id = 'MainContent_btnGenerateButton'

    driver.get(catering_order_url)

    start_date = WebDriverWait(driver, config.max_wait_time).until(expected_conditions.visibility_of_element_located((By.ID, start_date_id)))  

    end_date = driver.find_element(By.ID, end_date_id)

    submit = driver.find_element(By.ID, submit_id)

    start_date.click()
    time.sleep(2)
    pyautogui.press('backspace', presses=10)
    start_date.send_keys(date)

    end_date.click()
    time.sleep(2)
    pyautogui.press('backspace', presses=10)
    end_date.send_keys(date)

    time.sleep(5)

    submit.click()

    time.sleep(5)
