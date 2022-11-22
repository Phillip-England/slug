from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import pyautogui
import time


def daypart_activity(engine, date):

    try:
        engine.driver.get(engine.config.daypart_activity_url)
        start_date_input = WebDriverWait(engine.driver, engine.config.max_wait_time).until(expected_conditions.visibility_of_element_located((By.ID, engine.config.daypart_activity_start_date_id)))
        end_date_input = WebDriverWait(engine.driver, engine.config.max_wait_time).until(expected_conditions.visibility_of_element_located((By.ID, engine.config.daypart_activity_end_date_id)))
        submit_button = WebDriverWait(engine.driver, engine.config.max_wait_time).until(expected_conditions.visibility_of_element_located((By.ID, engine.config.daypart_activity_submit_id)))
        print(f'Page loaded at {engine.config.daypart_activity_url}')
    except:
        raise Exception(f'Failed to load page at {engine.config.daypart_activity_url}')

    # we could go through and create a failsafe for this next section by comparing our user-defined date to the text inside the date elements. If the dates do not match, the bot was too quick and needs to rerun the next section

    try:
        start_date_input.click()
        time.sleep(1)
        pyautogui.write(date)
        end_date_input.click()
        time.sleep(1)
        pyautogui.write(date)
        time.sleep(1)
        pyautogui.press('enter')
        submit_button.click()
        time.sleep(5)
        print(f'Pdf {engine.config.daypart_activity_default_download_path} downloaded at {engine.config.daypart_activity_url}')
    except:
        raise Exception(f'Failed to download pdf at {engine.config.daypart_activity_url}')


