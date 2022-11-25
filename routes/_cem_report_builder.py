import pyautogui
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

def cem_report_builder(engine, date):

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

        # sending the date in
        start_date_input.send_keys(date)
        end_date_input.send_keys(date)
        print(f'Date information entered at {engine.config.cem_report_builder_url}')

        # submitting data to pull
        cem_types = ['overall sat', 'taste', 'fast service', 'attentive', 'cleanliness com', 'order acc']
        pyautogui.click(engine.config.report_builder_cem_selection_cords)
        time.sleep(1)
        for cem in cem_types:
            pyautogui.write(cem, interval=engine.config.pyautogui_type_speed)
            pyautogui.press('enter')
        print(f'Cem scores selected at {engine.driver.current_url}')

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









    except Exception as error:
        engine.driver.close()
        raise SystemExit(error)





    
    engine.driver.get(engine.config.cem_report_builder_url)
    # print("Report Builder Loaded")



    # # selecting the correct report type
    # engine.wait_for_color(engine.config.cem_blue_banner_color, engine.config.cem_blue_banner_cords, 'cem_banner.png')   
    # report_type_dropdown = engine.driver.find_element(By.ID, 'rbReportTypeSEL')
    # report_type_dropdown.click()
    # time.sleep(0.5)
    # pyautogui.press('down', presses=6)
    # time.sleep(0.5)
    # pyautogui.press('enter')
    # time.sleep(2)
    # print("Full Scale Report Selected")

    # # picking scores to pull data on
    # cem_selection_area = engine.driver.find_element(By.ID, engine.config.cem_score_selection_id)
    # cem_selection_area.click()
    # time.sleep(0.5)
    # pyautogui.write('Overall Satisfaction', interval=0.2)
    # pyautogui.press('enter')
    # pyautogui.write('Taste', interval=0.2)
    # pyautogui.press('enter')
    # pyautogui.write('Fast Service', interval=0.2)
    # pyautogui.press('enter')
    # pyautogui.write('Attentive/', interval=0.2)
    # pyautogui.press('enter')
    # pyautogui.write('Cleanliness Com', interval=0.2)
    # pyautogui.press('enter')
    # pyautogui.write('Order Ac', interval=0.2)
    # pyautogui.press('enter')
    # print("Cem Scores Selected")

    # #picking the proper date range
    # cem_date_range_area = engine.driver.find_element(By.ID, engine.config.cem_date_range_id)
    # pyautogui.moveTo(100, 100, 2)
    # cem_date_range_area.click()
    # time.sleep(1)
    # pyautogui.press('down', presses=4)
    # time.sleep(0.2)
    # pyautogui.press('enter')
    # time.sleep(5)
    # print('Date Range Selected')

    # #building the report
    # submit_button = engine.driver.find_element(By.ID, engine.config.report_builder_button_id)
    # submit_button.click()
    # time.sleep(5)
    # print('CEM Report Built')

    # # opening the dowload menu
    # cem_download_menu_button = engine.driver.find_element(By.ID, engine.config.cem_download_menu_button)
    # cem_download_menu_button.click()
    # time.sleep(5)
    # print("CEM Download Menu Opened")


    # #selecting correct pdf option
    # cem_portrait_pdf_toggle = engine.driver.find_element(By.ID, engine.config.cem_portrait_pdf_id)
    # cem_portrait_pdf_toggle.click()
    # time.sleep(5)
    # cem_download_button = engine.driver.find_element(By.ID, engine.config.cem_download_button_id)
    # cem_download_button.click()
    # time.sleep(5)
    # print('CEM Current Month PDF Downloaded - "FullScale_Report.PDF"')
