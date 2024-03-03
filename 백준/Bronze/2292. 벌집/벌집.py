import sys
import math

n = int(sys.stdin.readline())

i = 1
while n > i*(i-1)*3 + 1:
    i += 1
print(i)