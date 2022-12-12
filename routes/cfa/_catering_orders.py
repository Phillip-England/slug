import os
import time
import pyautogui
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

def catering_orders(self, driver, config, date):

    driver.get(self.catering_order_url)

    start_date = WebDriverWait(driver, config.max_wait_time).until(expected_conditions.visibility_of_element_located((By.ID, self.catering_start_date_id)))  

    end_date = driver.find_element(By.ID, self.catering_end_date_id)

    submit = driver.find_element(By.ID, self.catering_submit_id)

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
