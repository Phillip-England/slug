import config
import directories
import routes
import data
import date
import messages

from ._run import run

class engine:
    def __init__(self, driver):
        self.driver = driver
        self.config = config.config()
        self.directories = directories.directories()
        self.routes = routes.routes()
        self.data = data.data()
        self.date = date.date()
        self.messages = messages.messages()
    
    def run(self): run(self)


        
        
        






             
  
        
        

