from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import pyautogui
import pyperclip
import time
import os


def daypart_activity(self, driver, config, date):

    # loading page and getting elements
    driver.get(self.daypart_activity_url)
    start_date_input = WebDriverWait(driver, config.max_wait_time).until(expected_conditions.visibility_of_element_located((By.ID, self.daypart_activity_start_date_id)))
    end_date_input = WebDriverWait(driver, config.max_wait_time).until(expected_conditions.visibility_of_element_located((By.ID, self.daypart_activity_end_date_id)))
    submit_button = WebDriverWait(driver, config.max_wait_time).until(expected_conditions.visibility_of_element_located((By.ID, self.daypart_activity_submit_id)))

    # entering date into date fields
    start_date_input.click()
    time.sleep(1)
    pyautogui.typewrite(date, config.pyautogui_type_speed)
    end_date_input.click()
    time.sleep(1)
    pyautogui.typewrite(date, config.pyautogui_type_speed)
    time.sleep(1)
    pyautogui.press('enter')

    # pdf download occurs here
    submit_button.click()
    time.sleep(5)



