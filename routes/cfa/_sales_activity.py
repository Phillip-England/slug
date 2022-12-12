from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys
import time
import os

def sales_activity(self, driver, config, date):
    
    # going to sales activity page
    driver.get(self.sales_activity_url)
    date_input = WebDriverWait(driver, config.max_wait_time).until(expected_conditions.visibility_of_element_located((By.ID, self.sales_activity_date_input_id)))
    submit_button = WebDriverWait(driver, config.max_wait_time).until(expected_conditions.visibility_of_element_located((By.ID, self.sales_activity_submit_id)))

    # sending date info
    date_input.send_keys(Keys.CONTROL + 'a')
    date_input.send_keys(Keys.DELETE)
    date_input.send_keys(date)

    # downloading and giving a second for pdf to download
    submit_button.click()
    time.sleep(5)

