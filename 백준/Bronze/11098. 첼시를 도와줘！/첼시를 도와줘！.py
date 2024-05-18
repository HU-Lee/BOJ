import sys

n = int(sys.stdin.readline())

for _ in range(n):
    p = int(sys.stdin.readline())
    max = 0
    tmp = ''
    for _ in range(p):
        c, name = sys.stdin.readline().split()
        c = int(c)
        if c > max:
            max = c
            tmp = name

    print(tmp)