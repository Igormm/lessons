import sys
import os
import ast

print("Input dictionary [{'key': value, }]:")
d1 = input()
_d1 = ast.literal_eval(d1)

max = max(_d1.values())
lt = []
for i in _d1.values():
 lt.append(i)

print(sorted(lt)[-3:])

