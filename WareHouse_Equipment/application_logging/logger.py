import logging.config


class App_Logger:
    def __init__(self, module):
        # preparing log configuration
        logging.config.fileConfig(fname='configuration/logging.conf',
                                  disable_existing_loggers=False)
        self.LOGGER = logging.getLogger(module)

    def log(self, logging_level, message):
        if logging_level == 'INFO':
            self.LOGGER.info(message)
        elif logging_level == 'ERROR':
            self.LOGGER.error(message)
