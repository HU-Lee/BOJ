import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

stack = []

for i in range(n):
    while stack and arr[stack[-1]] < arr[i]:
        arr[stack.pop()] = arr[i]
    stack.append(i)

while stack:
    arr[stack.pop()] = -1

print(*arr) 