import sys

arr = list(map(int, sys.stdin.readline().split()))

print(sum([i**2 for i in arr]) % 10)