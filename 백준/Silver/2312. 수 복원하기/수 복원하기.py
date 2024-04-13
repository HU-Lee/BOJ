import sys

t = int(sys.stdin.readline())

def analyze(n):
    x = 2
    cnt = 0
    while n >= x:
        if n % x == 0:
            n = n // x
            cnt += 1
        else:
            if cnt != 0:
                print(x, cnt)
            x += 1
            cnt = 0
    if cnt != 0:
        print(x, cnt)


for _ in range(t):
    n = int(sys.stdin.readline())
    analyze(n)