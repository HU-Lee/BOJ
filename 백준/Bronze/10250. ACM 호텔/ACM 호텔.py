import sys

t = int(sys.stdin.readline())
for _ in range(t):
    h, w, n = map(int, sys.stdin.readline().split())
    floor = n % h if n % h != 0 else h
    room = (n-1) // h + 1
    print(floor * 100 + room)