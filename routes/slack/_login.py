import os
import time
import pyautogui
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


def login(self, driver, config, account):


    driver.get(account.get('login_url'))

    slack_email_input = WebDriverWait(driver, config.max_wait_time).until(expected_conditions.visibility_of_element_located((By.ID, self.login_email_id)))

    slack_password_input = WebDriverWait(driver, config.max_wait_time).until(expected_conditions.visibility_of_element_located((By.ID, self.login_password_id)))

    slack_signin_button = WebDriverWait(driver, config.max_wait_time).until(expected_conditions.visibility_of_element_located((By.ID, self.login_submit_id)))

    slack_email_input.send_keys(account.get('email'))
    slack_password_input.send_keys(account.get('password'))

    slack_signin_button.click()

    time.sleep(2)

    pyautogui.press('enter')
