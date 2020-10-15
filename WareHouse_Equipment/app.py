import argparse
import os
import sys
import logging.config

from Validation.argument_validation import arg_validate
from application_logging.logger import App_Logger


class WareHouse:
    def __init__(self):
        self.logger = App_Logger('main')

    def __get_Arguments(self):
        arg_parser = argparse.ArgumentParser(
            formatter_class=argparse.RawTextHelpFormatter
        )
        arg_parser.add_argument('--image', '--im', '--i', help='image path for prediction', type=str)
        arg_parser.add_argument('--video','--v', help='video path for prediction', type=str)
        if len(sys.argv)!=3:
            arg_parser.print_help()
            sys.exit(-1)
        return  arg_parser

    def main(self):
        arg_parser = self.__get_Arguments()
        args = arg_parser.parse_args()
        print(args.image)
        if args.image!= None:
            arg_validate().isImageExists(args.image)
        print('hi')
        print(args.image)


if __name__ == "__main__":
    warehouse = WareHouse()
    warehouse.main()
