import sys

n = int(sys.stdin.readline().strip())

cnt = 0
while n > 0:
    cnt += n%2
    n //= 2

print(cnt)