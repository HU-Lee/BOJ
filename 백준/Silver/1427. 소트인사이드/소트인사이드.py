import sys

n = int(sys.stdin.readline().strip())
arr = [0] * 10

while n > 0:
    arr[n % 10] += 1
    n //= 10

ans = 0
left, mul = 0, 0

while left < 10:
    if arr[left] == 0:
        left += 1
        continue
    arr[left] -= 1
    ans += 10 ** mul * left
    mul += 1

print(ans)
