from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

def log_sales_data(engine):

    #visiting our sales tracking google form
    engine.driver.get(engine.config.sales_tracking_form_url)
    loading_element = WebDriverWait(engine.driver, engine.config.max_wait_time).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, engine.config.sales_form_input_class_name)))

    inputs = engine.driver.find_elements(By.CLASS_NAME, engine.config.sales_form_input_class_name)
    submit = engine.driver.find_elements(By.CLASS_NAME, engine.config.sales_form_submit_class_name)


    # exctracting inputs and inputting values
    date_input = inputs[0]
    date_input.send_keys(engine.data.daypart_activity.get('date'))

    day_input = inputs[1]
    day_input.send_keys(engine.data.daypart_activity.get('day'))

    breakfast_sales_input = inputs[2]
    breakfast_sales_input.send_keys(engine.data.daypart_activity.get('breakfast_sales'))

    lunch_sales_input = inputs[3]
    lunch_sales_input.send_keys(engine.data.daypart_activity.get('lunch_sales'))

    midshift_sales_input = inputs[4]
    midshift_sales_input.send_keys(engine.data.daypart_activity.get('midshift_sales'))

    dinner_sales_input = inputs[5]
    dinner_sales_input.send_keys(engine.data.daypart_activity.get('dinner_sales'))

    total_sales_input = inputs[6]
    total_sales_input.send_keys(engine.data.daypart_activity.get('total_sales'))

    breakfast_transactions_input = inputs[7]
    breakfast_transactions_input.send_keys(engine.data.daypart_activity.get('breakfast_transactions'))

    lunch_transactions_input = inputs[8]
    lunch_transactions_input.send_keys(engine.data.daypart_activity.get('lunch_transactions'))

    midshift_transactions_input = inputs[9]
    midshift_transactions_input.send_keys(engine.data.daypart_activity.get('midshift_transactions'))

    dinner_transactions_input = inputs[10]
    dinner_transactions_input.send_keys(engine.data.daypart_activity.get('dinner_transactions'))

    total_transactions_input = inputs[11]
    total_transactions_input.send_keys(engine.data.daypart_activity.get('total_transactions'))

    breakfast_check_average_input = inputs[12]
    breakfast_check_average_input.send_keys(engine.data.daypart_activity.get('breakfast_check_average'))

    lunch_check_average_input = inputs[13]
    lunch_check_average_input.send_keys(engine.data.daypart_activity.get('lunch_check_average'))

    midshift_check_average_input = inputs[14]
    midshift_check_average_input.send_keys(engine.data.daypart_activity.get('midshift_check_average'))

    dinner_check_average_input = inputs[15]
    dinner_check_average_input.send_keys(engine.data.daypart_activity.get('dinner_check_average'))

    total_check_average_input = inputs[16]
    total_check_average_input.send_keys(engine.data.daypart_activity.get('total_check_average'))

    carryout_sales_input = inputs[17]
    carryout_sales_input.send_keys(engine.data.sales_activity.get('carryout_sales'))

    cfa_delivery_sales_input = inputs[18]
    cfa_delivery_sales_input.send_keys(engine.data.sales_activity.get('cfa_delivery_sales'))

    curbside_sales_input = inputs[19]
    curbside_sales_input.send_keys(engine.data.sales_activity.get('curbside_sales'))

    delivery_sales_input = inputs[20]
    delivery_sales_input.send_keys(engine.data.sales_activity.get('delivery_sales'))

    dine_in_sales_input = inputs[21]
    dine_in_sales_input.send_keys(engine.data.sales_activity.get('dine_in_sales'))

    drive_thru_sales_input = inputs[22]
    drive_thru_sales_input.send_keys(engine.data.sales_activity.get('drive_thru_sales'))

    m_carryout_sales_input = inputs[23]
    m_carryout_sales_input.send_keys(engine.data.sales_activity.get('m_carryout_sales'))

    m_dine_in_sales_input = inputs[24]
    m_dine_in_sales_input.send_keys(engine.data.sales_activity.get('m_dine_in_sales'))

    m_drive_thru_sales_input = inputs[25]
    m_drive_thru_sales_input.send_keys(engine.data.sales_activity.get('m_drive_thru_sales'))

    on_demand_sales_input = inputs[26]
    on_demand_sales_input.send_keys(engine.data.sales_activity.get('on_demand_sales'))

    pickup_sales_input = inputs[27]
    pickup_sales_input.send_keys(engine.data.sales_activity.get('pickup_sales'))

    submit[0].click()
