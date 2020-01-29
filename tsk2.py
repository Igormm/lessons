import sys
import os

str1 = ''.join(sys.argv[1:])
str2 = os.path.basename(__file__)
resstr = {}

for i in str1:
 resstr[i] = str1.count(i)
print(resstr)
