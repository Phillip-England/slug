from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# local classes
import config
import directories
import logger
import routes
import data
import date

# class methods
from ._get_driver import get_driver
from ._wait_for_color import wait_for_color
from ._init_script import init_script
from ._run import run

class engine:
    def __init__(self):
        self.service = Service(ChromeDriverManager().install())
        self.options = Options()
        self.config = config.config()
        self.directories = directories.directories()
        self.logger = logger.logger()
        self.routes = routes.routes()
        self.data = data.data()
        self.date = date.date()
    
    def get_driver(self): get_driver(self)
    def wait_for_color(self, color, coordinates, filename): wait_for_color(self, color, coordinates, filename)
    def init_script(self): init_script(self)
    def run(self): run(self)


        
        
        






             
  
        
        

