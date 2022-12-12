import os
import time
import pyautogui
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


def send_message(self, driver, config, account, message):

    
    loading_element = WebDriverWait(driver, config.max_wait_time).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, self.chats_class_name)))   

    chats = driver.find_elements(By.CLASS_NAME, self.chats_class_name)

    for chat in chats:
        if chat.get_attribute('aria-label') == account.get('chat_aria_label'):
            selected_chat = chat

    selected_chat.click()

    time.sleep(2)

    message_input = WebDriverWait(driver, config.max_wait_time).until(expected_conditions.visibility_of_element_located((By.ID, account.get('message_input_id'))))   


    for line in message:
        if line == 'BREAK':
            pyautogui.hotkey('shift', 'enter')
        else:
            message_input.send_keys(line)

    pyautogui.press('enter')

    time.sleep(2)


        
 


