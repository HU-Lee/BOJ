import sys

n = int(sys.stdin.readline())
arr = []

for _ in range(n):
    arr.append(int(sys.stdin.readline()))

s = sum(arr)
if s % 2 == 0 and s // 2 in arr:
    print(s//2)
else:
    print("BAD")