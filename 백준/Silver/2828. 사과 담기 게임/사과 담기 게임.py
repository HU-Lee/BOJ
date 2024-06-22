import sys

n,m  = map(int,sys.stdin.readline().split())
c = int(sys.stdin.readline())

start = 1
end = m

ans = 0

for _ in range(c):
    x = int(sys.stdin.readline())
    if start <= x <= end:
        continue
    elif x < start:
        ans += start - x
        start = x
        end = x + m - 1
    elif x > end:
        ans += x - end
        end = x
        start = x - m + 1

print(ans)