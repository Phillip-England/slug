import os
import time
import pyautogui
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


def groupme_message(engine, message):
    
    loading_element = WebDriverWait(engine.driver, engine.config.max_wait_time).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, engine.config.groupme_chats_class_name)))   

    chats = engine.driver.find_elements(By.CLASS_NAME, engine.config.groupme_chats_class_name)

    # TESTING ENV
    if engine.config.testing_groupme == True:
        for chat in chats:
            if chat.get_attribute('aria-label') == engine.config.groupme_testing_aria_label:
                selected_chat = chat

        selected_chat.click()

        time.sleep(2)

        message_input = WebDriverWait(engine.driver, engine.config.max_wait_time).until(expected_conditions.visibility_of_element_located((By.ID, engine.config.groupme_testing_messaging_area_id)))   


        for line in message:
            if line == 'BREAK':
                pyautogui.hotkey('shift', 'enter')
            else:
                message_input.send_keys(line)

        pyautogui.press('enter')

        time.sleep(2)

    # NON_TESTING ENV
    else:
        for chat in chats:
            if chat.get_attribute('aria-label') == engine.config.groupme_southroads_leadership_aria_label:
                selected_chat = chat

        selected_chat.click()

        time.sleep(2)

        message_input = WebDriverWait(engine.driver, engine.config.max_wait_time).until(expected_conditions.visibility_of_element_located((By.ID, engine.config.groupme_southroads_leadership_messaging_area_id)))

        for line in message:
            if line == 'BREAK':
                pyautogui.hotkey('shift', 'enter')
            else:
                message_input.send_keys(line)

        pyautogui.press('enter')

        time.sleep(2)


        
 


