import sys

ones = [x*x for x in range(1, 240)]

arr = [4]*50001
for n in range(1, 50001):
    if n in ones:
        arr[n] = 1
    else:
        for x in ones:
            if x > n:
                break
            arr[n] = min(arr[n], arr[n - x] + 1)

n = int(sys.stdin.readline())
print(arr[n])