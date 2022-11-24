import pyautogui
import time
from selenium.webdriver.common.by import By

def cem_report_builder(engine):

    # going to CEM website
    engine.driver.get(engine.config.cem_url)
    print("CEM Login Succesful")
    engine.driver.get(engine.config.cem_report_builder_url)
    print("Report Builder Loaded")

    # selecting the correct report type
    engine.wait_for_color(engine.config.cem_blue_banner_color, engine.config.cem_blue_banner_cords, 'cem_banner.png')   
    report_type_dropdown = engine.driver.find_element(By.ID, 'rbReportTypeSEL')
    report_type_dropdown.click()
    time.sleep(0.5)
    pyautogui.press('down', presses=6)
    time.sleep(0.5)
    pyautogui.press('enter')
    time.sleep(2)
    print("Full Scale Report Selected")

    # picking scores to pull data on
    cem_selection_area = engine.driver.find_element(By.ID, engine.config.cem_score_selection_id)
    cem_selection_area.click()
    time.sleep(0.5)
    pyautogui.write('Overall Satisfaction', interval=0.2)
    pyautogui.press('enter')
    pyautogui.write('Taste', interval=0.2)
    pyautogui.press('enter')
    pyautogui.write('Fast Service', interval=0.2)
    pyautogui.press('enter')
    pyautogui.write('Attentive/', interval=0.2)
    pyautogui.press('enter')
    pyautogui.write('Cleanliness Com', interval=0.2)
    pyautogui.press('enter')
    pyautogui.write('Order Ac', interval=0.2)
    pyautogui.press('enter')
    print("Cem Scores Selected")

    #picking the proper date range
    cem_date_range_area = engine.driver.find_element(By.ID, engine.config.cem_date_range_id)
    pyautogui.moveTo(100, 100, 2)
    cem_date_range_area.click()
    time.sleep(1)
    pyautogui.press('down', presses=4)
    time.sleep(0.2)
    pyautogui.press('enter')
    time.sleep(5)
    print('Date Range Selected')

    #building the report
    submit_button = engine.driver.find_element(By.ID, engine.config.report_builder_button_id)
    submit_button.click()
    time.sleep(5)
    print('CEM Report Built')

    # opening the dowload menu
    cem_download_menu_button = engine.driver.find_element(By.ID, engine.config.cem_download_menu_button)
    cem_download_menu_button.click()
    time.sleep(5)
    print("CEM Download Menu Opened")


    #selecting correct pdf option
    cem_portrait_pdf_toggle = engine.driver.find_element(By.ID, engine.config.cem_portrait_pdf_id)
    cem_portrait_pdf_toggle.click()
    time.sleep(5)
    cem_download_button = engine.driver.find_element(By.ID, engine.config.cem_download_button_id)
    cem_download_button.click()
    time.sleep(5)
    print('CEM Current Month PDF Downloaded - "FullScale_Report.PDF"')
