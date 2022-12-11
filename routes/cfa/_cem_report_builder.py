import pyautogui
import time
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

def cem_report_builder(driver, config):

    cem_url_true = os.environ.get("CEM_TRUE_URL")
    main_logo_id = 'clientLogo'
    report_builder_url = os.environ.get("REPORT_BUILDER_URL")
    report_builder_button_id = 'rbBuildReportBTN'
    report_type_dropdown_id = 'rbReportTypeSEL'
    report_date_range_dropdown_id = 'rbDateRangeSEL'
    report_builder_start_date_id = 'rbStartDateTB'
    report_builder_end_date_id = 'rbEndDateTB'
    report_builder_cem_selection_class_name = 'default'
    report_builder_build_button_id = 'rbBuildReportBTN'
    report_builder_scores_loaded_id = 'rvTitleSpan1'
    cem_download_menu_button = 'rvSaveReportBTN'
    cem_download_menu_id = 'rvsTitleDiv'
    cem_portrait_pdf_id = 'rvsPDFLBL'
    cem_download_button_id = 'rvsDownloadBTN'

    # going to cem page
    driver.get(cem_url_true)
    main_logo = WebDriverWait(driver, config.max_wait_time).until(expected_conditions.visibility_of_element_located((By.ID, main_logo_id)))

    # loading the report builder page
    driver.get(report_builder_url)
    report_builder_button = WebDriverWait(driver, config.max_wait_time).until(expected_conditions.visibility_of_element_located((By.ID, report_builder_button_id)))
    report_type_input = WebDriverWait(driver, config.max_wait_time).until(expected_conditions.visibility_of_element_located((By.ID, report_type_dropdown_id)))

    # selecting full scale report
    report_type_input.send_keys('f')

    # confirming full scale report was selected
    start_date_input = WebDriverWait(driver, config.max_wait_time).until(expected_conditions.visibility_of_element_located((By.ID, report_builder_start_date_id)))
    end_date_input = WebDriverWait(driver, config.max_wait_time).until(expected_conditions.visibility_of_element_located((By.ID, report_builder_end_date_id)))
    report_type_dropdown = driver.find_element(By.ID, report_date_range_dropdown_id)

    # filtering out the cem selection input box
    elements_with_default_class_name = driver.find_elements(By.CLASS_NAME, report_builder_cem_selection_class_name)
    cem_selection_input = elements_with_default_class_name[1]
    cem_selection_input.click()

    # submitting data to pull
    cem_types = ['overall sat', 'taste', 'fast service', 'attentive', 'cleanliness com', 'order acc']
    for cem in cem_types:
        pyautogui.typewrite(cem, interval=config.pyautogui_type_speed)
        time.sleep(0.2)
        pyautogui.press('enter')

    report_types_to_build = ['current_month', 'ninty_day_rolling', 'year_to_date']

    for report in report_types_to_build:

        date_range_dropdown = driver.find_element(By.ID, report_date_range_dropdown_id)
        date_range_dropdown.click()
        time.sleep(0.2)

        if report == 'current_month':
            pyautogui.press('down', presses=4)
            pyautogui.press('enter')

        if report == 'ninty_day_rolling':
            pyautogui.press('up', presses=3)
            pyautogui.press('enter')

        if report == 'year_to_date':
            pyautogui.press('down', presses=6)
            pyautogui.press('enter')


        # building the report
        build_button = driver.find_element(By.ID, report_builder_build_button_id)
        build_button.click()

        # waiting for report to be built
        full_scale_report_title = WebDriverWait(driver, config.max_wait_time).until(expected_conditions.visibility_of_element_located((By.ID, report_builder_scores_loaded_id)))

        # opening the download menu
        save_export_button = driver.find_element(By.ID, cem_download_menu_button)
        save_export_button.click()

        # waiting for download menu to load
        cem_download_menu = WebDriverWait(driver, config.max_wait_time).until(expected_conditions.visibility_of_element_located((By.ID, cem_download_menu_id)))
        time.sleep(3)

        # selecting portrait pdf and downloading pdf
        portrait_option = driver.find_element(By.ID, cem_portrait_pdf_id)
        portrait_option.click()
        time.sleep(3)

        cem_download_pdf_button = WebDriverWait(driver, config.max_wait_time).until(expected_conditions.visibility_of_element_located((By.ID, cem_download_button_id)))
        cem_download_pdf_button.click()
        time.sleep(3)


