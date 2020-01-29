import sys
import os

str1 = ''.join(sys.argv[1:])
str2 = os.path.basename(__file__)

if str1 and len(str1) < 1000 and str1[0].isalpha():
 print(str1.title())
else:
 print (f'Usage: {str2} "name lastname"\nThe first argument must be wrapped with quotation marks " "\nString cannot be empty and don\'t containing over 1000 characters')
 
