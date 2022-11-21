import glob
import os
from datetime import datetime
import pyautogui

class logger:
    def __init__(self):
        pass

    def init_log(self, basepath, basename, extension):
        files = glob.glob(os.path.join(basepath, '*'))
        file_name = f'{basename}{len(files)}{extension}'
        file_path = os.path.join(basepath, file_name)
        return file_path
    
    def timestamp(self, path):
        file = open(path, 'a')
        file.write(f'{datetime.now()}\n')
        file.close()

    def set_master_log(self, file_path):
        self.master_log_path = file_path

    def master_log(self, message):
        file = open(self.master_log_path, 'a')
        file.write(f'{str(message)}\n')

    def screenshot(self, basepath, filename):
        image = pyautogui.screenshot(os.path.join(basepath, filename))
        return image


    