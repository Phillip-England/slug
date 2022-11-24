from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys
import pyautogui
import time
import os

def sales_activity(engine, date):
    
    try:

        # going to sales activity page
        engine.driver.get(engine.config.sales_activity_url)
        date_input = WebDriverWait(engine.driver, engine.config.max_wait_time).until(expected_conditions.visibility_of_element_located((By.ID, engine.config.sales_activity_date_input_id)))
        submit_button = WebDriverWait(engine.driver, engine.config.max_wait_time).until(expected_conditions.visibility_of_element_located((By.ID, engine.config.sales_activity_submit_id)))

        #checking for proper url
        if engine.driver.current_url == engine.config.sales_activity_url:
            print(f'Page loaded at {engine.config.sales_activity_url}')
        else:
            raise Exception(f'Failed to load page at {engine.config.sales_activity_url}')

        # inputting date via loop
        input_counter = 0
        while True:
            # sending date info
            date_input.send_keys(Keys.CONTROL + 'a')
            date_input.send_keys(Keys.DELETE)
            date_input.send_keys(date)
            input_counter = input_counter + 1
            # break out and continue if date input value is good
            if date_input.get_attribute('value') == date:
                print(f'Date information entered at {engine.config.sales_activity_url}')
                break
            # throw error on repeat
            if input_counter == engine.config.max_loop:
                raise Exception(f'Failed to input date at {engine.config.sales_activity_url}')
        
        # downloading pdf via loop
        input_counter = 0
        while True:

            # downloading and giving a second for pdf to download
            submit_button.click()
            time.sleep(5)
        
            # checking if pdf was properly downloaded
            if os.path.exists(engine.config.sales_activity_default_download_path) == True:
                print(f'{engine.config.sales_activity_default_download_path} downloaded at {engine.config.sales_activity_url}')
                break
            # if the pdf was not downloaded, we need to determine if we picked a bad day
            else:
                # checking if we got a pop up box, if we did, we picked a bad day
                bad_day_popup = engine.driver.find_element(By.ID, engine.config.sales_activity_bad_day_id)
                if bad_day_popup.is_displayed():
                    raise Exception(f'Selected a bad day at {engine.config.sales_activity_url}')

                # if we did not get a popup box, then we selected a good day, but our pdf took too long to download. We need to reloop through the process.
                input_counter = input_counter + 1
                # if we max out our loop, pdf failed to download
                if input_counter == engine.config.max_loop:
                    raise Exception(f'Failed to download pdf at {engine.config.sales_activity_url}')
    
    # logging errors
    except Exception as error:
        engine.driver.close()
        raise SystemExit(error)

