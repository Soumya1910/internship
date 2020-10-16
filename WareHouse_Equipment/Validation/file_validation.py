import os

from Exception.FileValidationException import FileValidationException
from application_logging.logger import App_Logger


class FileValidate():
    def __init__(self):
        self.logger = App_Logger('validation')

    def isFileExists(self, file_path):
        self.logger.log('INFO','Image Path : '+str(file_path))
        if os.path.isfile(file_path)==False:
            raise FileValidationException('File Not found : '+str(file_path))


    def checkFileSize(self, file_path):
        file_size = os.stat(file_path).st_size
        self.logger.log('INFO','File Size : '+str(file_size))
        if file_size == 0:
            raise FileValidationException('File is not proper. Please check')



    def fileValidation(self, file_path):
        absolute_path = os.path.abspath(file_path)
        self.isFileExists(absolute_path)
        self.checkFileSize(absolute_path)
