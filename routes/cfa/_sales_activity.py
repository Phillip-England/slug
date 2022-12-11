from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys
import time
import os

def sales_activity(driver, config, date):

    sales_activity_url = os.environ.get("SALES_ACTIVITY_URL")
    date_input_id = 'MainContent_cfaCommonReportInputInterface1_startBusinessDateWithTime_I'
    bad_day_id = 'InformationalPopup_HCB-1'
    submit_id = 'MainContent_cfaCommonReportInputInterface1_btnGenerateButton'
    
    # going to sales activity page
    driver.get(sales_activity_url)
    date_input = WebDriverWait(driver, config.max_wait_time).until(expected_conditions.visibility_of_element_located((By.ID, date_input_id)))
    submit_button = WebDriverWait(driver, config.max_wait_time).until(expected_conditions.visibility_of_element_located((By.ID, submit_id)))

    # sending date info
    date_input.send_keys(Keys.CONTROL + 'a')
    date_input.send_keys(Keys.DELETE)
    date_input.send_keys(date)

    # downloading and giving a second for pdf to download
    submit_button.click()
    time.sleep(5)

