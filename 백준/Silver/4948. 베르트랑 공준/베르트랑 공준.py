import sys

arr = [True]*250001

for i in range(2, 500):
    k = 2
    while i*k < 250001:
        arr[i*k] = False
        k += 1

while True:
    n = int(sys.stdin.readline())
    if n == 0:
        break
    cnt = sum(1 for i in range(n+1, 2*n+1) if arr[i])
    print(cnt)