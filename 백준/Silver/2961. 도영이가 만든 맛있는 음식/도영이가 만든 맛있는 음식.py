import sys
from functools import reduce

n = int(sys.stdin.readline())

arr = []
for _ in range(n):
    arr.append(list(map(int,sys.stdin.readline().split())))

ans = 10**9
path = []
def dfs(i):
    global ans
    if i == n:
        return
    else:
        path.append(arr[i])
        sour = 1
        for p in path:
            sour *= p[0]
        bitter = sum(map(lambda x: x[1], path))
        ans = min(ans,abs(sour-bitter))
        for j in range(i+1,n):
            dfs(j)
        path.pop()

for i in range(n):
    dfs(i)
print(ans)