import sys
import os

str1 = ''.join(sys.argv[1:])
str2 = os.path.basename(__file__)
usage = f'Usage: {str2} [set] [set] [set]'
a = []
b = set()

for iset in sys.argv[1:]:
 a.append(set(iset))

print(a)

print(a[0], type(a[0]))
print(a[1], type(a[1]))
print(a[-1], type(a[-1]))

if a[-1].isdisjoint(a[1]):
 print("Не содержат")
else:
 print("Содержат")
 if a[1].isdisjoint(a[-1]):
  print("Не содержат")
 else:
  print("Содержат")
