import sys

arr = [i for i in range(2, 10000)]

for a in range(2, 100):
    for idx, x in enumerate(arr):
        if x > a and x % a == 0:
            arr[idx] = 0

arr = [i for i in arr if i != 0]

m = int(sys.stdin.readline())
n = int(sys.stdin.readline())

arr = [i for i in arr if i >= m and i <= n]

if arr:
    print(sum(arr))
    print(arr[0])
else:
    print(-1)