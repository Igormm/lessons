import sys
import os
import ast

arg1 = sys.argv[1:]
str2 = os.path.basename(__file__)
usage = f'Usage: {str2}'

print("Input first dictionary [{'key': value, }]:")
d1 = input()
_d1 = ast.literal_eval(d1)
print("Input second dictionart [{'key': value, }]:")
d2 = input()
_d2 = ast.literal_eval(d2)

print(type(d1), type(d2), type(_d1), type(_d2))

_d2.update(_d1)

print(_d2)
