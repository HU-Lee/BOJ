import sys

n = int(sys.stdin.readline())

stack = []
for _ in range(n):
    arr = list(map(int, sys.stdin.readline().split()))
    if arr[0] == 1:
        stack.append(arr[1])
    elif arr[0] == 2:
        x = stack.pop() if stack else -1
        print(x)
    elif arr[0] == 3:
        print(len(stack))
    elif arr[0] == 4:
        print(0 if stack else 1)
    elif arr[0] == 5:
        if stack:
            print(stack[-1])
        else:
            print(-1)