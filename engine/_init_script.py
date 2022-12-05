import os

def init_script(self):

    #maximizing driver
    self.driver.maximize_window()

    # clear all files here
    self.directories.dump(self.directories.screenshots)
    self.directories.dump(self.directories.master_logs)
    self.directories.dump(self.directories.downloads)
