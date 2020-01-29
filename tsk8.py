import sys
import os
import ast

def remove_duplicates(l):
 return list(set(l))

def different_between_list(l, l1):
 return list(set(l) - set(l1))

remov_duplicates(sys.argv[1:])



