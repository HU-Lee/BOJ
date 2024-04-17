import sys

n = int(sys.stdin.readline())

if n in [1,3]:
    print(-1)
else:
    x,r = n // 5, n % 5
    if r in [0, 2, 4]:
        print(x  + r//2)
    else:
        print(x-1 + (r+5)//2)
