import os
import glob

class directories:

    def __init__(self):
        self.downloads = os.path.join(os.environ.get("HOME"), 'Downloads')

    def dump(self, path):
        files = glob.glob(os.path.join(path, '*'))
        for file in files: os.remove(file)

    def get_newest_file(self, path):
        files = glob.glob(os.path.join(path, '*'))
        return files[0]
        
    def delete_file(self, directory, filename):
        os.remove(os.path.join(directory, filename))

    def clear_downloads(self):
        self.dump(self.downloads)


