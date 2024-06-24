import sys

nums = [x for x in range(1000001)]

nums[0] = 0
nums[1] = 0

for i in range(2, 1002):
    x = 2*i
    while x < 1000001:
        nums[x] = 0
        x += i

m, n = map(int, sys.stdin.readline().split())

arr = [x for x in range(m, n+1) if nums[x] != 0]
for i in arr:
    print(i)