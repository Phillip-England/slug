import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import time
import pyautogui

def send_message(driver, config, account, message):

    loading_element_id = 'c-coachmark-anchor'
    message_element_class_name = 'ql-editor'
    schedule_button_class_name = 'c-button-unstyled'
    schedule_button_aria_label = 'Schedule for later'
    custom_time_button_class_name = 'c-menu_item__label'
    time_slot_class_name = 'c-select_input__content_text'
    schedule_message_button_class_name = 'c-button'

    driver.get(account[0].get('home_url'))

    slack_loading_element = WebDriverWait(driver, config.max_wait_time).until(expected_conditions.visibility_of_element_located((By.ID, loading_element_id)))

    message_input = driver.find_element(By.CLASS_NAME, message_element_class_name)

    message_input.click()

    for line in message:
        if line == 'BREAK':
            pyautogui.hotkey('shift', 'enter')
        else:
            message_input.send_keys(line)

    time.sleep(2)
    pyautogui.press('enter')
    time.sleep(1)