import sys

n,m = map(int, sys.stdin.readline().split())
arr = sorted(map(int, sys.stdin.readline().split()))

agg = []
def dfs(i):
    if i == m:
        print(' '.join(map(str, agg)))
        return
    for j in arr:
        if agg and agg[-1] > j:
            continue
        agg.append(j)
        dfs(i + 1)
        agg.pop()

dfs(0)