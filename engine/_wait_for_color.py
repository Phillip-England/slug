import time

def wait_for_color(self, color, coordinates, filename):
    max_wait_time = 10
    start = time.time()
    waiting = True
    while waiting:
        image = self.logger.screenshot(self.directories.screenshots, filename)
        pixel_color = image.getpixel(coordinates)
        if pixel_color == color:
            waiting = False
            self.logger.master_log(f'Screenshot for {filename} was successful in {time.time() - start} seconds')
            time.sleep(2)
        else:
            self.directories.delete_file(self.directories.screenshots, filename)
            elapsed_time = time.time() - start
            if elapsed_time > max_wait_time:
                self.logger.master_log(f'Session timed out waiting for screenshot {filename}')
                raise Exception('sessions timed out waiting for screenshot')
                