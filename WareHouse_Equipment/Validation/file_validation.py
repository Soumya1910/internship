import os

from Exception.FileValidationException import FileValidationException
from application_logging.logger import App_Logger


class FileValidate():
    def __init__(self):
        self.logger = App_Logger('file-validation')

    def isFileExists(self, file_path):
        self.logger.log('INFO', 'checking file exists or not..')
        if not os.path.isfile(file_path):
            raise FileValidationException('File Not found : ' + str(file_path))

    def checkFileSize(self, file_path):
        file_size = os.stat(file_path).st_size
        self.logger.log('INFO', 'Checking file size \tFile Size : ' + str(file_size))
        if file_size == 0:
            raise FileValidationException('File is not proper. Please check')

    def fileValidation(self, file_path):
        absolute_path = os.path.abspath(file_path)
        self.logger.log('INFO','Absolute File Path : '+absolute_path)
        self.isFileExists(absolute_path)
        self.checkFileSize(absolute_path)
