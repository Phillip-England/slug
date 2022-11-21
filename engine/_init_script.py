import os

def init_script(self):

    print("Initalizing Slug...")

    self.options.add_experimental_option('detach', False)


    # clear all files here
    self.directories.dump(self.directories.screenshots)
    self.directories.dump(self.directories.master_logs)
    # os.system("rm /home/phillip/Downloads/'Daypart Activity Report.pdf'")
    # os.system("rm /home/phillip/Downloads/FullScale_Report.PDF")

    # setting up the master log
    master_log = self.logger.init_log(self.directories.master_logs, 'log', '.txt')
    self.logger.timestamp(master_log)
    self.logger.set_master_log(master_log)
    self.logger.master_log('Starting Automation Script')

    #initalizing our chrome browser driver
    self.get_driver()
