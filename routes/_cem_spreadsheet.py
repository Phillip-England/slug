from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import os
import pyautogui
import time

def cem_spreadsheet(engine):
    
    try:

        # loading spreadsheet
        engine.driver.get(engine.config.cem_spreadsheet_url)
        sign_in_button = WebDriverWait(engine.driver, engine.config.max_wait_time).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, engine.config.cem_spreadsheet_loading_element_class_name)))
        print(f'Page loaded at {engine.driver.current_url}')

        # selecting download option
        pyautogui.hotkey('alt', 'f')
        time.sleep(0.5)
        pyautogui.press('down')
        time.sleep(0.5)
        pyautogui.press('enter')
        time.sleep(0.5)
        pyautogui.press('down')
        time.sleep(0.5)
        pyautogui.press('down')
        time.sleep(0.5)
        pyautogui.press('down')
        time.sleep(0.5)
        pyautogui.press('down')
        time.sleep(0.5)
        pyautogui.press('enter')
        time.sleep(5)

        # checking if csv was downloaded
        if os.path.exists(engine.config.cem_spreadsheet_download_path):
            print(f'Csv {engine.config.cem_spreadsheet_download_path} downloaded at {engine.driver.current_url}')
        else:
            raise Exception(f'Failed to download csv {engine.config.cem_spreadsheet_download_path} at {engine.driver.current_url}')

    except Exception as error:
        # logging errors    
        engine.driver.close()
        raise SystemExit(error)
