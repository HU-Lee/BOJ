import sys
import math

n,m = map(int,sys.stdin.readline().split())

arr = list(map(int,sys.stdin.readline().split()))

arr = list(reversed(sorted(arr))) + [0]

x = arr[0]
s = 0 

for idx, t in enumerate(arr):
    if t == x:
        continue
    else:
        if s + (x-t)*(idx) >= m:
            print(x - math.ceil((m-s)/(idx)))
            break
        else:
            s += (x-t)*(idx)
            x = t