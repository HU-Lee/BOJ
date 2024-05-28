import sys

n,m = map(int,sys.stdin.readline().split())

i = 1

ans = 0
while 2**(i-1) <= m:
    tmp = ans
    base = 2**i
    x1 = m // base
    r1 = m % base
    x2 = (n-1) // base
    r2 = (n-1) % base

    ans += (x1 - x2) * base // 2
    if r1 >= base // 2:
        ans += r1 - (base // 2 - 1)
    if r2 >= base // 2:
        ans -= r2 - (base // 2 - 1)
    i += 1

print(ans)