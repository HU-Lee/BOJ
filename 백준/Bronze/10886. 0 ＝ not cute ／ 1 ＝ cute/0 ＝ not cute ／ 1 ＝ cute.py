import sys

n = int(sys.stdin.readline())
sum = 0
for _ in range(n):
    sum += int(sys.stdin.readline())

print("Junhee is not cute!" if sum <= n//2 else "Junhee is cute!")