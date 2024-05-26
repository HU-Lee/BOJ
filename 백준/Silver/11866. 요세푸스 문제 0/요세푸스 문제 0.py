import sys
import collections

n,k = map(int,sys.stdin.readline().split())

q = collections.deque([i for i in range(1,n+1)])

deleted = []
while q:
    for _ in range(k-1):
        q.append(q.popleft())
    deleted.append(q.popleft())

print(f'<{", ".join(map(str,deleted))}>')