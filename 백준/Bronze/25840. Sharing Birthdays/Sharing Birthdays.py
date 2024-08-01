import sys
n = int(sys.stdin.readline())

births = set()
for _ in range(n):
    b = sys.stdin.readline().rstrip()
    births.add(b)

print(len(births))