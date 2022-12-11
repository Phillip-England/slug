from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import pyautogui
import pyperclip
import time
import os


def daypart_activity(driver, config, date):

    daypart_activity_url = os.environ.get("DAYPART_ACTIVITY_URL")
    start_date_id = 'MainContent_BusDate1_B-1Img'
    end_date_id = 'MainContent_BusDate2_B-1Img'
    submit_id = 'MainContent_btnGenerateButton'
    bad_day_id = 'InformationalPopup_HCB-1'

    # loading page and getting elements
    driver.get(daypart_activity_url)
    start_date_input = WebDriverWait(driver, config.max_wait_time).until(expected_conditions.visibility_of_element_located((By.ID, start_date_id)))
    end_date_input = WebDriverWait(driver, config.max_wait_time).until(expected_conditions.visibility_of_element_located((By.ID, end_date_id)))
    submit_button = WebDriverWait(driver, config.max_wait_time).until(expected_conditions.visibility_of_element_located((By.ID, submit_id)))

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



