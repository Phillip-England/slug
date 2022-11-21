from selenium import webdriver

def get_driver(self):
    self.driver = webdriver.Chrome(service=self.service, options=self.options)
    self.driver.maximize_window()