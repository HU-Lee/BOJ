import sys

a = int(sys.stdin.readline().strip())
b = int(sys.stdin.readline().strip())

for i in [b % 10, b // 10 % 10, b // 100, b]:
    print(a * i)