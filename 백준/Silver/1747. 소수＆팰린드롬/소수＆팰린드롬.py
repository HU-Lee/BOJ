import sys

arr = [1]*1210001
arr[0] = 0
arr[1] = 0

for i in range(2, 1101):
    for j in range(i*2, 1210001, i):
        if arr[j] == 1:
            arr[j] = 0

arr = list(idx for idx, val in enumerate(arr) if val == 1)
arr = list(filter(lambda x: str(x) == str(x)[::-1], arr))

ans = 0
n = int(sys.stdin.readline())
for i in arr:
    if i >= n:
        ans = i
        break

print(ans)