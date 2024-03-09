import sys

arr = list(map(int, sys.stdin.readline().split()))

base = [1,1,2,2,2,8]

ans = [str(base[i] - arr[i]) for i in range(6)]

print(" ".join(ans))