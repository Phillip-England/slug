import os
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


def hr_payroll(self, driver, config, date):

    driver.get(os.environ.get("CFA_HR_PAYROLL_URL"))

    all_reports = WebDriverWait(driver, config.max_wait_time).until(expected_conditions.visibility_of_element_located((By.ID, self.hr_all_reports_id)))

    all_reports.click()   

    bday_report = WebDriverWait(driver, config.max_wait_time).until(expected_conditions.visibility_of_element_located((By.ID, self.hr_bday_report_id)))

    bday_report.click()

    bday_report_loading_element = WebDriverWait(driver, config.max_wait_time).until(expected_conditions.visibility_of_element_located((By.ID, self.hr_bday_loading_element_id)))

    all_td_elements = driver.find_elements(By.TAG_NAME, 'td')

    for element in all_td_elements:
        print(element.text)

    time.sleep(2)
