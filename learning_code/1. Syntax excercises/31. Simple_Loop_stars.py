import sys
import math

n = 5
#print("Loop 1")
for i in range(1, n+1):
    print(" " * (n-i) + "*" * ((i*2)-1))

#print("Loop 2")
for i in range(0, n):
    print(" " * i + "*" * (((n-i)*2)-1))

