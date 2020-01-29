import sys
import os

str1 = ''.join(sys.argv[1:])
str2 = os.path.basename(__file__)

if len(str1) > 1:
 str3 = str1[:2]+ str1[-2:]
 print(str3)
else:
 print (f'Usage: {str2} [string] \n One character isnt string')
