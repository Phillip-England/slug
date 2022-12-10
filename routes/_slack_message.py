import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import time
import pyautogui

def slack_message(engine, message):

    try:

        if engine.config.testing_slack == True:
            engine.driver.get(os.environ.get("SLACK_TESTING"))
        else:
            engine.driver.get(os.environ.get("SLACK_CFASOUTHROADS"))

        pyautogui.press('enter')

        slack_loading_element = WebDriverWait(engine.driver, engine.config.max_wait_time).until(expected_conditions.visibility_of_element_located((By.ID, engine.config.slack_loading_element_id)))

        message_input = engine.driver.find_element(By.CLASS_NAME, engine.config.slack_message_element_class_name)

        message_input.click()


        for line in message:
            if line == 'BREAK':
                pyautogui.hotkey('shift', 'enter')
            else:
                message_input.send_keys(line)

        send_buttons = engine.driver.find_elements(By.CLASS_NAME, engine.config.slack_schedule_button_class_name)

        for button in send_buttons:
            if button.get_attribute('aria-label') == engine.config.slack_schedule_button_aria_label:
                schedule_button = button

        schedule_button.click()
        time.sleep(2)

        c_menu_items = engine.driver.find_elements(By.CLASS_NAME, engine.config.slack_custom_time_button_class_name)
        
        for element in c_menu_items:
            if element.text == 'Custom time':
                custom_time_button = element

        custom_time_button.click()

        time_slot = engine.driver.find_elements(By.CLASS_NAME, engine.config.slack_time_slot_class_name)

        time_slot[0].click()

        time.sleep(1)

        pyautogui.press('backspace')

        time.sleep(1)

        pyautogui.typewrite(engine.config.slack_scheduled_message_time, engine.config.pyautogui_type_speed)
        pyautogui.press('enter')
        time.sleep(2)

        buttons = engine.driver.find_elements(By.CLASS_NAME, engine.config.slack_schedule_message_button_class_name)

        for button in buttons:
            if button.get_attribute('data-qa') == 'schedule_message_dialog_submit_button':
                submit_button = button

        submit_button.click()

        time.sleep(10)            

    except Exception as error:
        engine.driver.close()
        raise SystemExit(error)