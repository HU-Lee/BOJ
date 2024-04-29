import sys

t = int(sys.stdin.readline())
stack = []
for _ in range(t):
    cmd = sys.stdin.readline().split()
    category = cmd[0]

    if category == 'push':
        x = int(cmd[1])
        stack.append(x)
    elif category == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
    elif category == 'size':
        print(len(stack))
    elif category == 'empty':
        print(1 if len(stack) == 0 else 0)
    elif category == 'top':
        print(stack[-1] if len(stack) > 0 else -1)