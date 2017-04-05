#!/bin/python3

import sys


n = int(input().strip())
a = []
for a_i in range(n):
    a_t = [int(a_temp) for a_temp in input().strip().split(' ')]
    a.append(a_t)
l = len(a[0])

diagOne = 0
diagTwo = 0

for i in range(l):
    diagOne += a[i][i]
for i in range(l-1,-1,-1):
    diagTwo += a[l-1-i][i]
print(abs(diagOne-diagTwo))