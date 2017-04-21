#!/bin/python3

import sys

S = input().strip()
'''The try statement attempts the operation inside the block. When an exception
is raised, the code stops and goes to the exception handler. For example, if the 
parsing operation here raises an exception, the value of S is not printed, and 
"Bad String" is printed instead.'''
try: 
    s = int(S)
    print(S)
except ValueError:
    print("Bad String")