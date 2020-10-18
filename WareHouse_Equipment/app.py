import argparse
import sys
from configparser import ConfigParser

from Exception.ArgumentParsingException import ArgumentParsingException
from Validation.file_validation import FileValidate
from Validation.image_validation import ImageValidate
from application_logging.logger import App_Logger


class WareHouse:
    def __init__(self):
        self.logger = App_Logger('main')
        self.config = ConfigParser()
        self.config.read('configuration/config.ini')

    def __get_Arguments(self):
        arg_parser = argparse.ArgumentParser(
            formatter_class=argparse.RawTextHelpFormatter
        )
        arg_parser.add_argument('--image', '--im', '--i', help='image path for prediction', type=str)
        arg_parser.add_argument('--video', '--v', help='video path for prediction', type=str)
        self.logger.log('INFO', 'Total arguments : ' + str(sys.argv))
        if len(sys.argv) != 3:
            arg_parser.print_help()
            raise ArgumentParsingException('')
            sys.exit(-1)
        return arg_parser

    def main(self):
        arg_parser = self.__get_Arguments()
        args = arg_parser.parse_args()

        if args.image is not None:
            FileValidate().fileValidation(args.image)
            prediction_file = ImageValidate().image_validation(args.image, self.config)
            self.logger.log('INFO', 'Prediction File Name : '+prediction_file)


if __name__ == "__main__":
    warehouse = WareHouse()
    warehouse.main()
