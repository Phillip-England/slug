from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import pyautogui
import time
import os


def daypart_activity(engine, date):

    try:

        # loading page and getting elements
        engine.driver.get(engine.config.daypart_activity_url)
        start_date_input = WebDriverWait(engine.driver, engine.config.max_wait_time).until(expected_conditions.visibility_of_element_located((By.ID, engine.config.daypart_activity_start_date_id)))
        end_date_input = WebDriverWait(engine.driver, engine.config.max_wait_time).until(expected_conditions.visibility_of_element_located((By.ID, engine.config.daypart_activity_end_date_id)))
        submit_button = WebDriverWait(engine.driver, engine.config.max_wait_time).until(expected_conditions.visibility_of_element_located((By.ID, engine.config.daypart_activity_submit_id)))

        # checking if page loaded properly
        if engine.driver.current_url == engine.config.daypart_activity_url:
            print(f'Page loaded at {engine.config.daypart_activity_url}')
        else:
            raise Exception(f'Failed to load page at {engine.config.daypart_activity_url}')

    # logging errors
    except Exception as error:
        engine.driver.close()
        raise SystemError(error)
        
    try:

        # entering date into date fields
        start_date_input.click()
        time.sleep(1)
        pyautogui.typewrite(date, engine.config.pyautogui_type_speed)
        end_date_input.click()
        time.sleep(1)
        pyautogui.typewrite(date, engine.config.pyautogui_type_speed)
        time.sleep(1)
        pyautogui.press('enter')
        # pdf download occurs here
        submit_button.click()
        time.sleep(5)

        # checking if pdf was downloaded
        if os.path.exists(engine.config.daypart_activity_default_download_path) == True:
            print(f'Pdf {engine.config.daypart_activity_default_download_path} downloaded at {engine.config.daypart_activity_url}')
        else:
            raise Exception(f"Failed to download pdf at {engine.config.daypart_activity_url}")

    # logging errors    
    except Exception as error:
        engine.driver.close()
        raise SystemExit(error)


