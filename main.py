from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from dotenv import load_dotenv
import platform

import engine

load_dotenv()

# works on my raspberry pi
if platform.platform() == 'Linux-5.15.76-v7l+-armv7l-with-glibc2.31':
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome()
else:
# works on my workstation computer
    options = Options()
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

engine = engine.engine(driver)

if __name__ == '__main__':
    print("Initalizing Slug...")
    engine.driver.maximize_window()
    engine.run()
    engine.driver.close()