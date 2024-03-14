import sys
from collections import deque

n,m = map(int,sys.stdin.readline().split())

world = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
ans = [[0 if world[i][j] == 0 else -1 for j in range(m)] for i in range(n)]
visited = [[False]*m for _ in range(n)]

arr = []
for i in range(n):
    for j in range(m):
        if world[i][j] == 2:
            arr.append((i,j,0))
            visited[i][j] = True

q = deque(arr)
while q:
    i,j,d = q.popleft()
    ans[i][j] = d
    for x,y in [(1,0),(-1,0),(0,1),(0,-1)]:
        i2 = i + x
        j2 = j + y
        if 0<=i2<n and 0<=j2<m and not visited[i2][j2] and world[i2][j2] == 1:
            q.append((i2,j2,d+1))
            visited[i2][j2] = True

for i in range(n):
    print(" ".join(map(str,ans[i])))