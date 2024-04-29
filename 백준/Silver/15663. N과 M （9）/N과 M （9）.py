import sys

n,m = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

agg = []
ans = set()
def dfs(i):
    if i == m:
        key = tuple(arr[x] for x in agg)
        ans.add(key)
    for j in range(n):
        if j in agg:
            continue
        agg.append(j)
        dfs(i + 1)
        agg.pop()

dfs(0)
ans = sorted(list(ans))
for v in ans:
    print(" ".join(map(str, v)))