import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import time
import pyautogui

def send_message(self, driver, config, account, message):


    driver.get(account[0].get('home_url'))

    slack_loading_element = WebDriverWait(driver, config.max_wait_time).until(expected_conditions.visibility_of_element_located((By.ID, self.loading_element_id)))

    message_input = driver.find_element(By.CLASS_NAME, self.message_element_class_name)

    message_input.click()

    for line in message:
        if line == 'BREAK':
            pyautogui.hotkey('shift', 'enter')
        else:
            message_input.send_keys(line)

    time.sleep(2)
    pyautogui.press('enter')
    time.sleep(1)