import os
import cv2

from Exception.FileValidationException import FileValidationException
from application_logging.logger import App_Logger


class ImageValidate():
    def __init__(self):
        self.logger = App_Logger('image-validation')

    def isImageFile(self, file_name, file_extension_list):
        extension = os.path.splitext(file_name)[1][1:].upper()
        self.logger.log('INFO', 'File Extension : ' + str(extension))
        file_extension_list = file_extension_list.split(',')
        if extension not in file_extension_list:
            raise FileValidationException('This is not an accepted image file')

    def isColorImageFile(self, file_name):
        image = cv2.imread(file_name)
        shape = image.shape
        self.logger.log('INFO', 'Image Size : ' + str(shape))
        if len(shape) != 3 or shape[2] != 3:
            raise FileValidationException('This is not a color image')

    def image_validation(self, file_name, file_extension_list):
        self.isImageFile(file_name, file_extension_list)
        self.isColorImageFile(file_name)
