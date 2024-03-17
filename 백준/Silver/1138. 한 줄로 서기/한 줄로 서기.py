import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

position = [i for i in range(n)]

ans = [0 for _ in range(n)]
for i, val in enumerate(arr):
    ans[position[val]] = i+1
    del position[val]

for i in ans:
    print(i, end=" ")
