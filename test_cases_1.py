from cases import Cases, log
from pathlib import Path
import time
import os


class TestCases1(Cases):
    def prep(self):
        if round(time.time()) % 2 != 0:
            log.warning("Number of seconds since the start of the Unix epoch, not a multiple of two")
        else:
            log.debug("Test case execution")

    def run(self):
        home_dir = Path.home()
        all_file_home_dir = os.listdir(home_dir)
        print(all_file_home_dir)

    def clean_up(self):
        pass
        log.info("No action required")
