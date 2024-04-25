import sys

n,m = map(int,sys.stdin.readline().split())
arr = sorted(map(int,sys.stdin.readline().split()))

ans = []

def dfs(l):
    if l == m:
        print(' '.join(map(str,ans)))
        return
    for i in range(n):
        if arr[i] not in ans:
            ans.append(arr[i])
            dfs(l+1)
            ans.pop()

dfs(0)