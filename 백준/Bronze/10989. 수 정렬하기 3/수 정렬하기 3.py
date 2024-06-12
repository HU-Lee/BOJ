import sys

n = int(sys.stdin.readline().strip())

arr = [0] * 10001

for _ in range(n):
    arr[int(sys.stdin.readline().strip())] += 1


for idx, val in enumerate(arr):
    for _ in range(val):
        print(idx)
