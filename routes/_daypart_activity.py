from selenium.webdriver.common.by import By
import pyautogui
import time
import os
import PyPDF2

def daypart_activity(self, engine):

    # going to daypart activity report url
    engine.driver.get(engine.config.daypart_activity_url)
    engine.wait_for_color(engine.config.daypart_activity_wage_input_color, engine.config.daypart_activity_wage_input_cords, 'wage_input.png')
    print("Daypart activity Page Loaded")

    # selecting proper start and end dates
    start_date_dropdown = engine.driver.find_element(By.ID, engine.config.daypart_activity_start_date_id)
    end_date_dropdown = engine.driver.find_element(By.ID, engine.config.daypart_activity_end_date_id)
    start_date_dropdown.click()
    time.sleep(1)
    pyautogui.press('left')
    pyautogui.press('enter')
    end_date_dropdown.click()
    time.sleep(1)
    pyautogui.press('left')
    pyautogui.press('enter')
    time.sleep(1)
    print("Date Range Selected for Daypart Activity")

    # clicking submit and downloading the report
    submit_button = engine.driver.find_element(By.ID, engine.config.daypart_activity_submit_id)
    submit_button.click()
    time.sleep(1)
    print("Daypart Activity Report Downloaded")


