import sys
import os

c = 0
larg = []
str2 = os.path.basename(__file__)
usage = f'Usage: {str2} [string] [string] [string] ... \n One character isnt string'

print(sys.argv)

for arg in sys.argv[1:]:
 if len(arg) > 1:
  larg.append(arg)
for larg in larg:
 if larg[0] == larg[-1]:
  c = c + 1
print(c)
print(usage, "not friendly: \n> are same from a given list of strings.")

