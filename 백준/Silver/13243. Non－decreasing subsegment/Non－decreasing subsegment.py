import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

ans = (0,0)

tmp = 0
s = 0
for i in range(n):
    if i == 0 or arr[i] >= arr[i-1]:
        tmp += 1
        s += arr[i]
    else:
        tmp = 1
        s = arr[i]
    if ans[0] < tmp:
        ans = (tmp, s)

print(ans[0], ans[1])