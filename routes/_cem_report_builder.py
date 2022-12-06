import pyautogui
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

def cem_report_builder(engine):

    try:

        # loading cem page which redirects
        engine.driver.get(engine.config.cem_url_true)
        cem_main_logo = WebDriverWait(engine.driver, engine.config.max_wait_time).until(expected_conditions.visibility_of_element_located((By.ID, engine.config.cem_loaded_id)))

        # checking if page loaded correctly
        if engine.driver.current_url == engine.config.cem_url_redirect:
            print(f'Page loaded at {engine.config.cem_url_redirect}')
        else:
            print(f'Page failed to load at {engine.config.cem_url_redirect}')
    
        # loading the report builder page
        engine.driver.get(engine.config.cem_report_builder_url)
        report_builder_button = WebDriverWait(engine.driver, engine.config.max_wait_time).until(expected_conditions.visibility_of_element_located((By.ID, engine.config.report_builder_button_id)))
        report_type_input = WebDriverWait(engine.driver, engine.config.max_wait_time).until(expected_conditions.visibility_of_element_located((By.ID, engine.config.report_type_dropdown_id)))

        # checking if page loaded correctly
        if engine.driver.current_url == engine.config.cem_report_builder_url:
            print(f'Page loaded at {engine.config.cem_report_builder_url}')
        else:
            print(f'Page failed to load at {engine.config.cem_report_builder_url}')

        # selecting full scale report
        report_type_input.send_keys('f')

        # confirming full scale report was selected
        start_date_input = WebDriverWait(engine.driver, engine.config.max_wait_time).until(expected_conditions.visibility_of_element_located((By.ID, engine.config.report_builder_start_date_id)))
        end_date_input = WebDriverWait(engine.driver, engine.config.max_wait_time).until(expected_conditions.visibility_of_element_located((By.ID, engine.config.report_builder_end_date_id)))
        report_type_dropdown = engine.driver.find_element(By.ID, engine.config.report_date_range_dropdown_id)

        # filtering out the cem selection input box
        elements_with_default_class_name = engine.driver.find_elements(By.CLASS_NAME, engine.config.report_builder_cem_selection_class_name)
        cem_selection_input = elements_with_default_class_name[1]
        cem_selection_input.click()

        # submitting data to pull
        cem_types = ['overall sat', 'taste', 'fast service', 'attentive', 'cleanliness com', 'order acc']
        for cem in cem_types:
            pyautogui.typewrite(cem, interval=engine.config.pyautogui_type_speed)
            time.sleep(0.2)
            pyautogui.press('enter')
        print(f'Cem scores selected at {engine.driver.current_url}')

        report_types_to_build = ['current_month', 'ninty_day_rolling', 'year_to_date']

        for report in report_types_to_build:

            date_range_dropdown = engine.driver.find_element(By.ID, engine.config.report_date_range_dropdown_id)
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
            build_button = engine.driver.find_element(By.ID, engine.config.report_builder_build_button_id)
            build_button.click()

            # waiting for report to be built
            full_scale_report_title = WebDriverWait(engine.driver, engine.config.max_wait_time).until(expected_conditions.visibility_of_element_located((By.ID, engine.config.report_builder_scores_loaded_id)))
            print(f'Full scale report built at {engine.driver.current_url}')

            # opening the download menu
            save_export_button = engine.driver.find_element(By.ID, engine.config.cem_download_menu_button)
            save_export_button.click()

            # waiting for download menu to load
            cem_download_menu = WebDriverWait(engine.driver, engine.config.max_wait_time).until(expected_conditions.visibility_of_element_located((By.ID, engine.config.cem_download_menu_id)))
            print(f'Cem download menu loaded at {engine.driver.current_url}')
            time.sleep(3)

            # selecting portrait pdf and downloading pdf
            portrait_option = engine.driver.find_element(By.ID, engine.config.cem_portrait_pdf_id)
            portrait_option.click()
            time.sleep(3)

            cem_download_pdf_button = WebDriverWait(engine.driver, engine.config.max_wait_time).until(expected_conditions.visibility_of_element_located((By.ID, engine.config.cem_download_button_id)))
            cem_download_pdf_button.click()
            time.sleep(3)

    except Exception as error:
        engine.driver.close()
        raise SystemExit(error)

