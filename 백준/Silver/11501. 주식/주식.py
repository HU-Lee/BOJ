import sys

t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    arr = list(map(int, sys.stdin.readline().split()))
    stack = []
    revenue = 0
    for idx, val in enumerate(arr):
        if not stack or stack[-1][1] >= val:
            stack.append((idx, val))
        else:
            while stack and stack[-1][1] < val:
                stack.pop()
            stack.append((idx, val))

    # print(stack)
    sell = (stack[0][0] + 1)*stack[0][1]
    for i in range(1, len(stack)):
        sell += (stack[i][0] - stack[i-1][0])*stack[i][1]
    revenue = sell - sum(arr)

    print(revenue)