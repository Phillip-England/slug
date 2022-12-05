from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from dotenv import load_dotenv
import platform

import engine

load_dotenv()

if platform.platform() == 'Linux-5.15.76-v7l+-armv7l-with-glibc2.31':
    options = webdriver.ChromeOptions()
    driver = webdriver.Remote(command_executor='https://172.17.0.2:4444', options = options)
else:
    options = Options()
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

engine = engine.engine(driver)

if __name__ == '__main__':
    print("Initalizing Slug...")
    engine.run()