import sys

n,m = map(int,sys.stdin.readline().split())
arr = []

def dfs(x, l):
    if l == m:
        print(' '.join(map(str,arr)))
        return
    for i in range(x,n+1):
        arr.append(i)
        dfs(i,l+1)
        arr.pop()

for i in range(1,n+1):
    arr.append(i)
    dfs(i,1)
    arr.pop()