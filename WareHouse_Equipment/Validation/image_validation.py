import os
import cv2
import random
import string

from Exception.FileValidationException import FileValidationException
from application_logging.logger import App_Logger


class ImageValidate():
    def __init__(self):
        self.logger = App_Logger('image-validation')

    def isImageFile(self, file_name, file_extension_list):
        extension = os.path.splitext(file_name)[1][1:].upper()
        file_extension_list = file_extension_list.split(',')
        self.logger.log('INFO', 'Valid File Extensions : ' + str(file_extension_list))
        if extension not in file_extension_list:
            raise FileValidationException('This is not an accepted image file')

    def isColorImageFile(self, file_name):
        self.logger.log('INFO','Validating color image or not..')
        image = cv2.imread(file_name)
        shape = image.shape
        self.logger.log('INFO', 'Image Size : ' + str(shape))
        if len(shape) != 3 or shape[2] != 3:
            raise FileValidationException('This is not a color image')

    def image_file_conversion_and_save(self, file_name, image_save_path):
        self.logger.log('INFO','Image File Conversion and save into particular directory..')
        image_file_name = os.path.basename(file_name).split('.')[0]
        random_string = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(8))
        save_file_name = image_file_name + '_' + random_string + '.jpg'
        image = cv2.imread(file_name)
        cv2.imwrite(image_save_path + '/' + save_file_name, image)
        return image_save_path + '/' + save_file_name

    def image_validation(self, file_name, config):
        file_extension_list = config.get('image', 'valid_image')
        image_save_path = config.get('image', 'image_store_path')
        self.isColorImageFile(file_name)
        self.isImageFile(file_name, file_extension_list)
        prediction_file = self.image_file_conversion_and_save(file_name, image_save_path)
        return prediction_file

