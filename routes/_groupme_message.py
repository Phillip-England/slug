import os
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


def groupme_message(engine):
    
    loading_element = WebDriverWait(engine.driver, engine.config.max_wait_time).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, engine.config.groupme_chats_class_name)))   

    chats = engine.driver.find_elements(By.CLASS_NAME, engine.config.groupme_chats_class_name)


    if engine.config.testing_groupme == True:
        for chat in chats:
            if chat.get_attribute('aria-label') == engine.config.groupme_testing_aria_label:
                selected_chat = chat
    else:
        print('Need to include aria label for cfa group me')   

    selected_chat.click()

    time.sleep(2)


