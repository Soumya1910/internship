import os

class ImageValidate():
    def __init__(self):
        pass

    def isImageFile(self, file_name):
        extension = os.path.splitext(file_name)[1][1:]
        print(extension)