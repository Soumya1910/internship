import os
import sys

from application_logging.logger import App_Logger


class arg_validate():
    def __init__(self):
        self.logger = App_Logger('validation')

    def isImageExists(self, image_path):
        self.logger.log('Image Path : '+str(image_path))
        absolute_path = os.path.abspath(image_path)
        if ~os.path.isfile(absolute_path):
            self.logger.log('File not found : '+str(absolute_path))
            sys.exit(-1)
