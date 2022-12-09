from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# local classes
import config
import directories
import routes
import data
import date
import scripts
import messages

# class methods
from ._run import run

class engine:
    def __init__(self, driver):
        self.driver = driver
        self.config = config.config()
        self.directories = directories.directories()
        self.routes = routes.routes()
        self.data = data.data()
        self.date = date.date()
        self.scripts = scripts.scripts()
        self.messages = messages.messages()
    
    def run(self): run(self)


        
        
        






             
  
        
        

