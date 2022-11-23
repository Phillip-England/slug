import pyautogui
import time

def log_sales_data(engine):

    #visiting our sales tracking google form
    engine.driver.get(engine.config.sales_tracking_form_url)
    engine.wait_for_color(engine.config.sales_form_purple_color, engine.config.sales_form_purple_header_cords, 'sales_form_input.png')

    #selecting the first input and using tab thereafter to navigate through the form
    pyautogui.click(engine.config.first_sales_input_cords)
    time.sleep(1)

    # business day and date
    pyautogui.typewrite(engine.data.previous_business_day_sales_data.get('business_date'), engine.config.pyautogui_type_speed)
    pyautogui.press('tab')
    time.sleep(0.5)
    pyautogui.typewrite(engine.data.previous_business_day_sales_data.get('day_of_week'), engine.config.pyautogui_type_speed)
    pyautogui.press('tab')
    time.sleep(0.5)

    # breakfast sales data
    pyautogui.typewrite(engine.data.previous_business_day_sales_data.get('breakfast_sales'), engine.config.pyautogui_type_speed)
    pyautogui.press('tab')
    time.sleep(0.5)
    pyautogui.typewrite(engine.data.previous_business_day_sales_data.get('breakfast_check_average'), engine.config.pyautogui_type_speed)
    pyautogui.press('tab')
    time.sleep(0.5)
    pyautogui.typewrite(engine.data.previous_business_day_sales_data.get('breakfast_transactions'), engine.config.pyautogui_type_speed)
    pyautogui.press('tab')
    time.sleep(0.5)

    #lunch sales data
    pyautogui.typewrite(engine.data.previous_business_day_sales_data.get('lunch_sales'), engine.config.pyautogui_type_speed)
    pyautogui.press('tab')
    time.sleep(0.5)
    pyautogui.typewrite(engine.data.previous_business_day_sales_data.get('lunch_check_average'), engine.config.pyautogui_type_speed)
    pyautogui.press('tab')
    time.sleep(0.5)
    pyautogui.typewrite(engine.data.previous_business_day_sales_data.get('lunch_transactions'), engine.config.pyautogui_type_speed)
    pyautogui.press('tab')
    time.sleep(0.5)

    #midshift sales data
    pyautogui.typewrite(engine.data.previous_business_day_sales_data.get('midshift_sales'), engine.config.pyautogui_type_speed)
    pyautogui.press('tab')
    time.sleep(0.5)
    pyautogui.typewrite(engine.data.previous_business_day_sales_data.get('midshift_check_average'), engine.config.pyautogui_type_speed)
    pyautogui.press('tab')
    time.sleep(0.5)
    pyautogui.typewrite(engine.data.previous_business_day_sales_data.get('midshift_transactions'), engine.config.pyautogui_type_speed)
    pyautogui.press('tab')
    time.sleep(0.5)

    #dinner sales data
    pyautogui.typewrite(engine.data.previous_business_day_sales_data.get('dinner_sales'), engine.config.pyautogui_type_speed)
    pyautogui.press('tab')
    time.sleep(0.5)
    pyautogui.typewrite(engine.data.previous_business_day_sales_data.get('dinner_check_average'), engine.config.pyautogui_type_speed)
    pyautogui.press('tab')
    time.sleep(0.5)
    pyautogui.typewrite(engine.data.previous_business_day_sales_data.get('dinner_transactions'), engine.config.pyautogui_type_speed)
    pyautogui.press('tab')
    time.sleep(1)
    pyautogui.press('enter')

    # giving page time to submit data
    time.sleep(5)