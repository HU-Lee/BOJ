import sys

n,m = map(int,sys.stdin.readline().split())

arr = list(map(int,sys.stdin.readline().split()))

q = [i+1 for i in range(n)]

ans = 0

for i in range(m):
    nxt = q.index(arr[i])
    ans += nxt if nxt <= len(q)//2 else len(q)-nxt
    q = q[nxt+1:]+q[:nxt]

print(ans)