from random import randbytes
from cases import Cases, log
import psutil
import os


class TestCases2(Cases):
    def prep(self):
        if psutil.virtual_memory().total < 3 * 1024:
            log.warning("RAM less than one gigabyte")

    def run(self):
        with open("test.txt", "wb") as test:
            size = randbytes(1024)
            test.write(size)

    def clean_up(self):
        os.remove("test.txt")
