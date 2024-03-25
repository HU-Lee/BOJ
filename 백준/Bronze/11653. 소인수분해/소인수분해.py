import sys

n = int(sys.stdin.readline().strip())

x = 2
while n != 1:
    if n % x == 0:
        n = n // x
        print(x)
    else:
        x += 1