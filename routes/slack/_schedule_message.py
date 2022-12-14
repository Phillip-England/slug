import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import time
import pyautogui

def schedule_message(self, driver, config, account, message):


    driver.get(account.get('home_url'))

    slack_loading_element = WebDriverWait(driver, config.max_wait_time).until(expected_conditions.visibility_of_element_located((By.ID, self.loading_element_id)))

    message_input = driver.find_element(By.CLASS_NAME, self.message_element_class_name)

    message_input.click()

    for line in message:
        if line == 'BREAK':
            pyautogui.hotkey('shift', 'enter')
        else:
            message_input.send_keys(line)

    send_buttons = driver.find_elements(By.CLASS_NAME, self.schedule_button_class_name)

    for button in send_buttons:
        if button.get_attribute('aria-label') == self.schedule_button_aria_label:
            schedule_button = button

    schedule_button.click()
    time.sleep(2)

    c_menu_items = driver.find_elements(By.CLASS_NAME, self.custom_time_button_class_name)
    
    for element in c_menu_items:
        if element.text == 'Custom time':
            custom_time_button = element

    custom_time_button.click()

    time_slot = driver.find_elements(By.CLASS_NAME, self.time_slot_class_name)

    time_slot[0].click()

    time.sleep(1)

    pyautogui.press('backspace')

    time.sleep(1)

    pyautogui.typewrite(config.slack_scheduled_message_time, config.pyautogui_type_speed)
    pyautogui.press('enter')
    time.sleep(2)

    buttons = driver.find_elements(By.CLASS_NAME, self.schedule_message_button_class_name)

    for button in buttons:
        if button.get_attribute('data-qa') == 'schedule_message_dialog_submit_button':
            submit_button = button

    submit_button.click()

    time.sleep(5)            