import sys

a,b = map(int, sys.stdin.readline().split())
c = int(sys.stdin.readline())
n = int(sys.stdin.readline())

if c < a:
    print(0)
elif c == a:
    print(0 if b >= 0 else 1)
else:
    x = b/(c-a)
    print(1 if n >= x else 0)