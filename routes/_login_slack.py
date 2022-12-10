import os
import time
import pyautogui
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


def login_slack(engine, account):

    engine.driver.get(account)

    slack_email_input = WebDriverWait(engine.driver, engine.config.max_wait_time).until(expected_conditions.visibility_of_element_located((By.ID, engine.config.slack_email_input_id)))

    slack_password_input = WebDriverWait(engine.driver, engine.config.max_wait_time).until(expected_conditions.visibility_of_element_located((By.ID, engine.config.slack_password_input_id)))

    slack_signin_button = WebDriverWait(engine.driver, engine.config.max_wait_time).until(expected_conditions.visibility_of_element_located((By.ID, engine.config.slack_sign_in_button_id)))

    slack_email_input.send_keys(os.environ.get("SLACK_EMAIL"))
    slack_password_input.send_keys(os.environ.get("SLACK_PASSWORD"))

    slack_signin_button.click()

    time.sleep(5)

    pyautogui.press('enter')