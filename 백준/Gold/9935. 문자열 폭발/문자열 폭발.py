import sys

s = sys.stdin.readline().strip()
pung = sys.stdin.readline().strip()
n = len(pung)

stack = []
for i in s:
    stack.append(i)
    while stack[-n:] == list(pung):
        for _ in range(n):
            stack.pop()

if stack:
    print("".join(stack))
else:
    print("FRULA")

