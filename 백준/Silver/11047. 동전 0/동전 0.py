import sys

n,x = map(int, sys.stdin.readline().strip().split())
arr = []
for _ in range(n):
    arr.append(int(sys.stdin.readline().strip()))

s = 0
for i in reversed(arr):
    s += x // i
    x = x % i

print(s)
