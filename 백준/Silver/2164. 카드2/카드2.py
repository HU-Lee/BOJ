import sys
from collections import deque

n = int(sys.stdin.readline())

queue = deque([i for i in range(1, n+1)])

while len(queue) > 1:
    queue.popleft()
    queue.append(queue[0])
    queue.popleft()

print(queue[0])

## deque를 씁시다...