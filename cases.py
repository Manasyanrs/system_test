import logger

log = logger.get_logger()


class Cases:
    def __init__(self, tc_id, name):
        self.tc_id = tc_id
        self.name = name

    def prep(self):
        pass

    def run(self):
        pass

    def clean_up(self):
        pass

    def execute(self):
        try:
            self.prep()
        except Exception as e:
            log.error("Error on preparation method")
            log.error(e)

        try:
            self.run()
        except Exception as e:
            log.error("Error on run method")
            log.error(e)

        try:
            self.clean_up()
        except Exception as e:
            log.error("Error on clean_up method")
            log.error(e)
