import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

arr.sort()

print(sum(x*(len(arr)-i) for i, x in enumerate(arr)))