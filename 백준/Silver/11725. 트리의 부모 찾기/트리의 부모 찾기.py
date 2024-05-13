import sys
import collections

sys.setrecursionlimit(10**6)

graph = collections.defaultdict(list)

n = int(sys.stdin.readline())

for _ in range(n - 1):
    x, y = map(int, sys.stdin.readline().split())
    graph[x].append(y)
    graph[y].append(x)  

arr = [0] * (n + 1)
def dfs(x):
    for i in graph[x]:
        if arr[i] == 0:
            arr[i] = x
            dfs(i)

dfs(1)
for i in range(2, n + 1):
    print(arr[i])