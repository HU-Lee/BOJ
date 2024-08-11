import sys

r,c = map(int,sys.stdin.readline().split())
a,b = map(int,sys.stdin.readline().split())

for i in range(r):
    if i % 2 == 0:
        for _ in range(a):
            print(('X'*b + '.'*b)*(c//2) + 'X'*b*(c%2))
    else:
        for _ in range(a):
            print(('.'*b + 'X'*b)*(c//2) + '.'*b*(c%2))
