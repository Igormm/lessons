import sys
import os

arg1 = sys.argv[1]
arg2 = sys.argv[2]
str2 = os.path.basename(__file__)
usage = f'Usage: {str2} count key [digit] value * [digit]'
dic = {}
x = int(arg2)

if arg1.isdigit() and arg2.isdigit():

 for i in range(0, int(arg1)+1):
  x = x * 2
  dic[i] = x
else: 
 print(usage)

print(dic)
