from application_logging.logger import App_Logger


class ArgumentParsingException(Exception):
    def __init__(self, message):
        # Call the base class constructor with the parameters it needs
        super().__init__(message)
        self.message = message
        self.logger = App_Logger('validation')
        self.logger.log('ERROR', message)