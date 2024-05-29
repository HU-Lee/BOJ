import sys

n = int(sys.stdin.readline())
arr = list(map(int,sys.stdin.readline().split()))

s = sum(arr)

ans = 0
for num in arr:
    s -= num
    ans += num * s

print(ans)