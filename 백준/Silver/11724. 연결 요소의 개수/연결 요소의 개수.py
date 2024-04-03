import sys
import collections

n,m = map(int, sys.stdin.readline().split())

graph = collections.defaultdict(list)

for _ in range(m):
    a,b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

arr = [i for i in range(n+1)]

for i in range(1,n+1):
    if arr[i] == i:
        q = [i]
        visited = [False] * (n+1)
        visited[i] = True
        while q:
            x = q.pop()
            for y in graph[x]:
                if not visited[y]:
                    visited[y] = True
                    arr[y] = arr[i]
                    q.append(y)

print(len(set(arr[1:])))