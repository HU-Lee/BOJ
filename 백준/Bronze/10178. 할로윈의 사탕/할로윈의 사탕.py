import sys

t = int(sys.stdin.readline())
for _ in range(t):
    n,m = map(int,sys.stdin.readline().split())
    print(f'You get {n//m} piece(s) and your dad gets {n%m} piece(s).')