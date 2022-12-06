import os

def init_script(self):

    #maximizing driver
    self.driver.maximize_window()

    # clear all files here
    if self.config.clear_downloads == True:
        self.directories.dump(self.directories.downloads)
