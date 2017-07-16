# import string
# import itertools
# from itertools import product
#
# letter = list(string.ascii_lowercase) + ['-']
#
# test = ['a', 'b', 'c']
#
# keywords = [''.join(i) for i in itertools.product(test, repeat = 3)]
#
#
# print(keywords)
#
# print()



import re
DATA = "Hey, you - what are you doing here!?"
print (re.findall(r"\w+", DATA))