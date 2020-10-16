import os

str='../abfhf.jpg'

extension = os.path.splitext(str)[1][1:].upper()
print(extension)