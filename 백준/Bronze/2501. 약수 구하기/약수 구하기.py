import sys
import math

n, k = map(int, sys.stdin.readline().split())

arr = set()
for x in range(1, int(math.sqrt(n))+1):
    if n % x == 0:
        arr.add(x)
        arr.add(n//x)

arr = list(sorted(arr))
if k > len(arr):
    print(0)
else:
    print(arr[k-1])