import os
import glob

class directories:

    def __init__(self):
        self.project = os.path.join(os.environ.get('HOME'), 'Desktop', 'Projects', 'auto')
        self.screenshots = os.path.join(self.project, 'screenshots')
        self.logs = os.path.join(self.project, 'logs')
        self.master_logs = os.path.join(self.logs, 'master')
        self.downloads = os.path.join(os.environ.get("HOME"), 'Downloads')

    def dump(self, path):
        files = glob.glob(os.path.join(path, '*'))
        for file in files: os.remove(file)

    def get_newest_file(self, path):
        files = glob.glob(os.path.join(path, '*'))
        return files[0]
        
    def delete_file(self, directory, filename):
        os.remove(os.path.join(directory, filename))

