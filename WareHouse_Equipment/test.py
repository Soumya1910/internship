import os
import random


import random, string
x = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(8))
print(x)

str='../abfhf.jpg'

extension = os.path.basename(str).split('.')[0]


print(extension)

