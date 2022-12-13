import os
import glob

class directories:

    def __init__(self):
        self.downloads = os.path.join(os.environ.get("HOME"), 'Downloads')
        self.cem_current_month_download_path = os.path.join(os.environ.get('HOME'), 'Downloads', 'FullScale_Report.PDF')
        self.cem_ninty_day_rolling_download_path = os.path.join(os.environ.get('HOME'), 'Downloads', 'FullScale_Report (1).PDF')
        self.cem_year_to_date_download_path = os.path.join(os.environ.get('HOME'), 'Downloads', 'FullScale_Report (2).PDF')
        self.daypart_activity_download_path = os.path.join(os.environ.get('HOME'), 'Downloads', 'Daypart Activity Report.pdf')
        self.sales_activity_download_path = os.path.join(os.environ.get('HOME'), 'Downloads', 'Sales Activity Report.pdf')
        self.catering_download_path = os.path.join(os.environ.get("HOME"), 'Downloads', 'Deferred Orders Reports.pdf')

    def dump(self, path):
        files = glob.glob(os.path.join(path, '*'))
        for file in files: os.remove(file)

    def get_newest_file(self, path):
        files = glob.glob(os.path.join(path, '*'))
        return files[0]
        
    def delete_file(self, directory, filename):
        if os.path.exists(os.path.join(directory, filename)):
            os.remove(os.path.join(directory, filename))

    def clear_downloads(self):
        self.dump(self.downloads)


