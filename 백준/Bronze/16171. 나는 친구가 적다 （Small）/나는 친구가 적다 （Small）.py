import sys

s = sys.stdin.readline().strip()
t = sys.stdin.readline().strip()

for n in "0123456789":
    s = s.replace(n, "")

print(1 if t in s else 0)