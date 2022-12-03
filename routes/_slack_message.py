import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import time
import pyautogui

def slack_message(engine, message):

    try:
        engine.driver.get(os.environ.get("SLACK_LOGIN_PAGE"))

        slack_email_input = WebDriverWait(engine.driver, engine.config.max_wait_time).until(expected_conditions.visibility_of_element_located((By.ID, engine.config.slack_email_input_id)))

        slack_password_input = WebDriverWait(engine.driver, engine.config.max_wait_time).until(expected_conditions.visibility_of_element_located((By.ID, engine.config.slack_password_input_id)))

        slack_signin_button = WebDriverWait(engine.driver, engine.config.max_wait_time).until(expected_conditions.visibility_of_element_located((By.ID, engine.config.slack_sign_in_button_id)))

        slack_email_input.send_keys(os.environ.get("SLACK_EMAIL"))
        slack_password_input.send_keys(os.environ.get("SLACK_PASSWORD"))

        slack_signin_button.click()

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

        pyautogui.press('down', presses=2)
        time.sleep(2)

        pyautogui.press('enter')
        time.sleep(2)

        pyautogui.press('tab', presses=3)
        time.sleep(2)

        pyautogui.typewrite(engine.config.slack_scheduled_message_time, engine.config.pyautogui_type_speed)
        pyautogui.press('enter')
        time.sleep(2)

        pyautogui.press('tab', presses=2)
        time.sleep(2)
        
        pyautogui.press('enter')

        time.sleep(10)



        
            


    except Exception as error:
        engine.driver.close()
        raise SystemExit(error)