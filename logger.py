import logging
from logging import Formatter


def get_logger():

    log = logging.getLogger(__name__)
    log.setLevel(logging.DEBUG)
    handler = logging.FileHandler("log.txt", encoding="utf-8")
    handler.setFormatter(Formatter(fmt='[%(asctime)s: %(filename)s %(levelname)s] %(message)s'))
    log.addHandler(handler)
    return log
