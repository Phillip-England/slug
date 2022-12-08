import os
import time
import pyautogui
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

def send_faith_message(engine):

    engine.driver.maximize_window()

    engine.driver.get(os.environ.get('TEXT_FREE_WEBSITE'))

    username_input = WebDriverWait(engine.driver, engine.config.max_wait_time).until(expected_conditions.visibility_of_element_located((By.ID, engine.config.text_free_username_id)))

    username_input.send_keys(os.environ.get("TEXT_FREE_USERNAME"))

    password_input = engine.driver.find_element(By.ID, engine.config.text_free_password_id)

    password_input.send_keys(os.environ.get("TEXT_FREE_PASSWORD"))

    time.sleep(0.2)

    pyautogui.press('enter')

    time.sleep(3)

    logo = WebDriverWait(engine.driver, engine.config.max_wait_time).until(expected_conditions.visibility_of_element_located((By.ID, engine.config.text_free_logo_id)))

    if engine.driver.find_element(By.ID, engine.config.text_free_close_google_contact_id):
        engine.driver.find_element(By.ID, engine.config.text_free_close_google_contact_id).click()

    compose = engine.driver.find_element(By.ID, engine.config.text_free_compose_id)
    compose.click()

    number_input = engine.driver.find_element(By.ID, engine.config.text_free_contact_input_id)

    number_input.send_keys(os.environ.get('PERSONAL_PHONE_NUMBER'))
    number_input.send_keys(',')

    pyautogui.press('tab')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)

    pyautogui.press('tab')
    time.sleep(1)
    pyautogui.typewrite(engine.data.get_random_faith_message(engine), interval=engine.config.pyautogui_type_speed)
    time.sleep(1)
    pyautogui.press('enter')


    # message_input = engine.driver.find_element(By.CLASS_NAME, engine.config.text_free_message_input_class_name)

    # message_input.click()

    # pyautogui.typewrite('testing', interval=engine.config.pyautogui_type_speed)

    # submit = engine.driver.find_element(By.ID, engine.config.text_free_send_button)

    # submit.click()

    time.sleep(20)


    